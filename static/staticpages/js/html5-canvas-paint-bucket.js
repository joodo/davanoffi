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

/*jslint browser: true */
/*global G_vmlCanvasManager, $ */

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

			while (pixelStack.length) {
				newPos = pixelStack.pop();
				x = newPos[0];
				y = newPos[1];

				// Get current pixel position
				pixelPos = (y * canvasWidth + x) * 4;
				//alert("1");
				// Go up as long as the color matches and are inside the canvas
				while (y >= drawingBoundTop && matchStartColor(pixelPos, startR, startG, startB)) {
					y -= 1;
					pixelPos -= canvasWidth * 4;
				}
				y += 1;
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

			checkPass();
		},

        checkPass = function () {
            var p1 = convertPos(609, 639),
                p2 = convertPos(552, 684),
                p3 = convertPos(566, 730),
                p4 = convertPos(492, 1022),
                p5 = convertPos(588, 940),
                p6 = convertPos(628, 910),
                p7 = convertPos(672, 1000);

            if (colorLayerData.data[p1] === 153 && colorLayerData.data[p1+1] === 0 && colorLayerData.data[p1+2] === 0 &&
                colorLayerData.data[p2] === 153 && colorLayerData.data[p2+1] === 76 && colorLayerData.data[p2+2] === 0 &&
                colorLayerData.data[p3] === 153 && colorLayerData.data[p3+1] === 153 && colorLayerData.data[p3+2] === 0 &&
                colorLayerData.data[p4] === 76 && colorLayerData.data[p4+1] === 0 && colorLayerData.data[p4+2] === 153 &&
                colorLayerData.data[p5] === 153 && colorLayerData.data[p5+1] === 0 && colorLayerData.data[p5+2] === 76 &&
                colorLayerData.data[p6] === 152 && colorLayerData.data[p6+1] === 0 && colorLayerData.data[p6+2] === 153 &&
                colorLayerData.data[p7] === 153 && colorLayerData.data[p7+1] === 0 && colorLayerData.data[p7+2] === 76
                ) {
                console.log("PASS!!!");
				setCookie("passport", "123-10-121112", 1);
                $("#mask").fadeIn(3500, function () {
                    window.location.href = blog_index_url
                });
            }
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