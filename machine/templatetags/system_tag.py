from django import template

register = template.Library()

@register.filter
def in_status(obj, status):
    return obj.filter(status=status)


@register.filter
def in_machine_type(obj, machine_type):
    return obj.filter(machine_type=machine_type)