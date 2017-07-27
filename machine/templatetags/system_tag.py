from django import template

register = template.Library()

@register.filter
def in_status(obj, status):
    return obj.filter(status=status)


@register.filter
def in_machine_type(obj, machine_type):
    return obj.filter(machine_type=machine_type)


@register.filter
def in_repair(obj):
    return obj.all().exclude(status='CLOSED')


@register.assignment_tag
def repair_pending(obj):
	print (obj.all().count())
	return obj.all().exclude(status='CLOSED').count()