from django import template

register = template.Library()


@register.simple_tag
def get_toasts_delay(message):
    message_str = str(message)
    word_count = len(message_str.split())
    delay = word_count * 500
    return delay if delay > 3000 else 3000
