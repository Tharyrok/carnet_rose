# encoding: utf-8

from django.contrib import admin

from admin_views.admin import AdminViews

from django.conf.locale.en import formats as en_formats

from reversion.admin import VersionAdmin

from .models import Movement

from .models import TestModel

en_formats.DATE_FORMAT = "Y-m-d"


class MovementAdmin(VersionAdmin):
    fieldsets = (
        (None, {
            "fields": (("date", "amount"), ("title", "kind"), ("comment",), ("bank_id",))
        }),
    )

    list_display = ("date", "title_column", "credit_column", "debit_column")

    def debit_column(self, obj):
        if obj.kind == "debit":
            return obj.amount
        return ""

    debit_column.short_description = "Débit"

    def credit_column(self, obj):
        if obj.kind == "credit":
            return obj.amount
        return ""

    credit_column.short_description = "Crédit"

    def title_column(self, obj):
        if obj.comment:
            return "%s [has comment]" % obj.title
        return obj.title

    title_column.short_description = "Title"

class FooTestAdmin(AdminViews):
    admin_views = (
            # ('Process This', 'process'),              # Admin view
            ('Go to LJW', 'http://www.ljworld.com'),  # Direct URL
    )

    # def process(self, *args, **kwargs):
    #     return redirect('http://www.cnn.com')


admin.site.register(Movement, MovementAdmin)
admin.site.register(TestModel, FooTestAdmin)
