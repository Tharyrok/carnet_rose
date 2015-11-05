from django import template
from django.db.models import Sum

from ..models import Movement


register = template.Library()


def sum_movements(**kwargs):
    credit = Movement.objects.filter(kind="credit", **kwargs).aggregate(Sum("amount"))["amount__sum"]
    debit =  Movement.objects.filter(kind="debit", **kwargs).aggregate(Sum("amount"))["amount__sum"]

    if credit is None:
        credit = 0

    if debit is None:
        debit = 0

    return credit - debit

@register.simple_tag
def current_year_total(year):
    return sum_movements(date__year=year)
