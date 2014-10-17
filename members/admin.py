# encoding: utf-8

import reversion
from django.contrib import admin
from .models import Member


class IsStillMember(admin.SimpleListFilter):
    title = 'Est membre'
    parameter_name = 'is_member'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Oui'),
            ('no', 'Non'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(member_end__isnull=True)

        if self.value() == 'no':
            return queryset.filter(member_end__isnull=False)


class MemberAdmin(reversion.VersionAdmin):
    list_display = ('first_name', 'last_name', 'last_paid_date', 'ca_member')
    list_filter = ('last_paid_date', 'ca_member', IsStillMember)
    radio_fields = {"juridical_form": admin.HORIZONTAL}
    search_fields = ('first_name', 'last_name')
    fieldsets = (
        ('Information générales', {
            'fields': (('first_name', 'last_name',), ('address', 'email'), ('juridical_form', 'billing_id')),
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
