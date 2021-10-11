from re import sub

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def url_to_string(url):
    return sub(r'.*?://', '', url)
