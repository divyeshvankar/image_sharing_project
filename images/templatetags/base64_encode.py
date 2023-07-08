from django import template
import base64

register = template.Library()

@register.simple_tag
def base64_encode(binary_data):
    return base64.b64encode(binary_data).decode('utf-8')
