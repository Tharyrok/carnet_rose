import re
from django import template
from django.conf import settings


numeric_test = re.compile("^\d+$")
register = template.Library()

@register.filter
def get_field(entry, field):
    """Gets an attribute of an object dynamically from a string name"""

    if field.name in entry.field_dict:
        if field.choices:
            return getattr(entry.object, "get_%s_display" % field.name)()
        return entry.field_dict[field.name]
    else:
        return settings.TEMPLATE_STRING_IF_INVALID


@register.filter
def only_existing(fields_list, entry):
    for i in fields_list:
        if entry.field_dict[i.name]:
            yield i
