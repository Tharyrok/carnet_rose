import reversion
from django.contrib import admin
from .models import Member


class MemberAdmin(reversion.VersionAdmin):
    list_display = ('first_name', 'last_name', 'last_paid_date')


admin.site.register(Member, MemberAdmin)
