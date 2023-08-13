from django.template import Library
from blog import models

register = Library()


@register.filter
def instance_of(value):
    return isinstance(value).__name__


@register.filter
def is_ticket(value):
    return isinstance(value, models.Ticket)


@register.filter
def is_review(value):
    return isinstance(value, models.Review)
