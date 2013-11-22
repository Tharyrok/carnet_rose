# encoding: utf-8

import reversion
from django.contrib import admin
from .models import Member


class MemberAdmin(reversion.VersionAdmin):
    list_display = ('first_name', 'last_name', 'last_paid_date', 'ca_member')
    list_filter = ('last_paid_date', 'ca_member', )
    radio_fields = {"juridical_form": admin.HORIZONTAL}
    fieldsets = (
        ('Information générales', {
            'fields': (('first_name', 'last_name',), ('address', 'email'), 'juridical_form'),
        }),
        ('Cotisation', {
            'fields': (('member_since', 'last_paid_date'),),
        }),
        ('Conseil d\'administration', {
            'fields': (('ca_member', 'ca_function'),),
        }),
        ('Résignation', {
            'fields': ('member_end', 'why_member_end'),
            'classes': ('collapse',),
        }),
    )


admin.site.register(Member, MemberAdmin)
