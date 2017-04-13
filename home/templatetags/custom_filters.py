from django import template

register = template.Library()


@register.filter
def field_type(field):
    return field.field.widget.__class__.__name__;


@register.filter
def full_name(user):
    return ' '.join([user.first_name, user.last_name])
