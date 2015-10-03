// Copyright 2010 William Malone (www.williammalone.com)
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

var paintBucketApp = (function () {
	"use strict";
	var context,
		canvasWidth,
		canvasHeight,
		curColor = {r: 0, g: 0, b: 0},
		drawingAreaX = 0,
		drawingAreaY = 0,
		drawingAreaWidth,
		drawingAreaHeight,
		colorLayerData,
		outlineLayerData,
        colorInfo={},

		// Clears the canvas.
		clearCanvas = function () {
			context.clearRect(0, 0, context.canvas.width, context.canvas.height);
		},

		matchOutlineColor = function (r, g, b, a) {
		    return (r === 255 && g === 255 && b === 255 || a === 0);
		},

		matchStartColor = function (pixelPos, startR, startG, startB) {
			var r = outlineLayerData.data[pixelPos],
				g = outlineLayerData.data[pixelPos + 1],
				b = outlineLayerData.data[pixelPos + 2],
				a = outlineLayerData.data[pixelPos + 3];

			// If current pixel of the outline image is black
			if (matchOutlineColor(r, g, b, a)) {
				return false;
			}

			r = colorLayerData.data[pixelPos];
			g = colorLayerData.data[pixelPos + 1];
			b = colorLayerData.data[pixelPos + 2];

			// If the current pixel matches the clicked color
			if (r === startR && g === startG && b === startB) {
				return true;
			}

			// If current pixel matches the new color
			if (r === curColor.r && g === curColor.g && b === curColor.b) {
				return false;
			}

			return false;
		},

		colorPixel = function (pixelPos, r, g, b, a) {
			colorLayerData.data[pixelPos] = r;
			colorLayerData.data[pixelPos + 1] = g;
			colorLayerData.data[pixelPos + 2] = b;
			colorLayerData.data[pixelPos + 3] = a !== undefined ? a : 255;
		},

		floodFill = function (startX, startY, startR, startG, startB) {
			var newPos,
				x,
				y,
				pixelPos,
				reachLeft,
				reachRight,
				drawingBoundLeft = drawingAreaX,
				drawingBoundTop = drawingAreaY,
				drawingBoundRight = drawingAreaX + drawingAreaWidth - 1,
				drawingBoundBottom = drawingAreaY + drawingAreaHeight - 1,
				pixelStack = [[startX, startY]];

            var maxX = -1, maxY = -1;
			while (pixelStack.length) {
				newPos = pixelStack.pop();
				x = newPos[0];
				y = newPos[1];

				// Get current pixel position
				pixelPos = (y * canvasWidth + x) * 4;
				// Go up as long as the color matches and are inside the canvas
				while (y >= drawingBoundTop && matchStartColor(pixelPos, startR, startG, startB)) {
					y -= 1;
					pixelPos -= canvasWidth * 4;
				}
				y += 1;
                if (y > maxY) {
                    maxY = y;
                    maxX = x;
                } else if (y == maxY && x > maxX) {
                    maxX = x;
                }

				pixelPos += canvasWidth * 4;

				reachLeft = false;
				reachRight = false;

				// Go down as long as the color matches and in inside the canvas
				while (y <= drawingBoundBottom && matchStartColor(pixelPos, startR, startG, startB)) {
					y += 1;

					colorPixel(pixelPos, curColor.r, curColor.g, curColor.b);

					if (x > drawingBoundLeft) {
						if (matchStartColor(pixelPos - 4, startR, startG, startB)) {
						    if (!reachLeft) {
						        // Add pixel to stack
								pixelStack.push([x - 1, y]);
								reachLeft = true;
							}
						} else if (reachLeft) {
							reachLeft = false;
						}
					}

					if (x < drawingBoundRight) {
						if (matchStartColor(pixelPos + 4, startR, startG, startB)) {
							if (!reachRight) {
								// Add pixel to stack
								pixelStack.push([x + 1, y]);
								reachRight = true;
							}
						} else if (reachRight) {
							reachRight = false;
						}
					}

					pixelPos += canvasWidth * 4;
				}
			}

            colorInfo[maxX+","+maxY] = curColor.r+","+curColor.g+","+curColor.b;
		},

		// Start painting with paint bucket tool starting from pixel specified by startX and startY
		paintAt = function (startX, startY) {
		    if (curColor.r + curColor.g + curColor.b === 0) {
		        return;
		    }

			var pixelPos = (startY * canvasWidth + startX) * 4,
				r = colorLayerData.data[pixelPos],
				g = colorLayerData.data[pixelPos + 1],
				b = colorLayerData.data[pixelPos + 2],
				a = colorLayerData.data[pixelPos + 3];

			if (r === curColor.r && g === curColor.g && b === curColor.b) {
				// Return because trying to fill with the same color
				return;
			}

			if (matchOutlineColor(r, g, b, a)) {
				// Return because clicked outline
				return;
			}

			floodFill(startX, startY, r, g, b);

			context.putImageData(colorLayerData, 0, 0);

            console.log(JSON.stringify(colorInfo));
			checkPass();
		},

        checkPass = function () {
            $.post(check_url, colorInfo, function(data,status) {
                var jump_url = url_dict[data]
                console.log(data+jump_url);
                if (jump_url) {
                    $("#mask").fadeIn(3500, function () {
                        window.location.href = jump_url
                    });
                }
            });
        },

        convertPos = function (x, y) {
            var dx = Math.round(x * canvasWidth / 1173);
            var dy = Math.round(y * canvasHeight / 1173);
            var pos = (dy * canvasWidth + dx) * 4;

            return pos;
        },

        setColor = function (r, g, b) {
            curColor.r = r;
            curColor.g = g;
            curColor.b = b;
        },

		// Creates a canvas element, loads images, adds events, and draws the canvas for the first time.
		init = function (canvas) {
		    context = canvas.getContext("2d");
		    canvasWidth = canvas.width;
		    canvasHeight = canvas.height;

		    outlineLayerData = context.getImageData(0, 0, canvasWidth, canvasHeight);
		    colorLayerData = context.getImageData(0, 0, canvasWidth, canvasHeight);

		    drawingAreaHeight = canvasHeight;
		    drawingAreaWidth = canvasWidth;
		};

	return {
	    init: init,
	    paintAt: paintAt,
	    setColor: setColor
	};
}());
