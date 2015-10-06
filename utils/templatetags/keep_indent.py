import math

from django import template
from django.utils.safestring import mark_safe
from django.utils import html


register = template.Library()


@register.filter()
def keep_indent(value):
    value = html.escape(value)
    value = value.replace(' ', '&nbsp;').replace('\n', '<br />')
    return mark_safe(value)

@register.simple_tag()
def get_css_opacity(last_life):
    if last_life > 1000:
        return 'onMouseOver="postMouseOver(this)" onMouseLeave="postMouseLeave(this)"'

    last_life = 0 if last_life < 0 else last_life/10
    opacity = math.log10(last_life+1)/2.1 + 0.05
    css = 'style="opacity:%f;" \
           onMouseOver="postMouseOver(this); opacityChange(this, 1);" \
           onMouseLeave="postMouseLeave(this); opacityChange(this,%f);"' %\
          (opacity, opacity)
    return css
