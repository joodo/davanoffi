from django import template
from django.utils.safestring import mark_safe
from django.utils import html


register = template.Library()


@register.filter()
def keep_indent(value):
    value = html.escape(value)
    value = value.replace(' ', '&nbsp;').replace('\n', '<br />')
    return mark_safe(value)
