import datetime
from django import template

register = template.Library()


@register.simple_tag
def horarido():
    return datetime.datetime.now().strftime("%H:%M:%S")
