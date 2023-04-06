from django import template
from decimal import Decimal

register = template.Library()


def get_month_total(month_totals, mode, month):
    if mode in month_totals and month in month_totals[mode]:
        return month_totals[mode][month]
    return ''


@register.filter
def get_dict_value(dictionary, key):
    if isinstance(dictionary, dict):
        return dictionary.get(key, '')
    return ''


@register.filter
def sort_months(month_totals):
    # get all the month names from month_totals
    month_names = set()
    for mode in month_totals.keys():
        for month in month_totals[mode].keys():
            month_names.add(month)

    # create a sorted list of month names
    sorted_month_names = sorted(list(month_names),
                                key=lambda x: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                               'September', 'October', 'November', 'December'].index(x))

    return sorted_month_names


@register.filter
def get_mode_total(month_totals, mode):
    total = 0
    if mode in month_totals:
        for month_total in month_totals[mode].values():
            total += month_total
    return total


@register.filter
def get_mode_month_total(month_totals, mode, month):
    if mode in month_totals and month in month_totals[mode]:
        return month_totals[mode][month]
    return ''


@register.filter
def sumofvalues(data_dict, key):
    return sum(Decimal(str(d.get(key, 0))) for d in data_dict)


@register.filter
def keyvalue(dictionary, key):
    return dictionary.get(key, '')


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_filter(data, key):
    return data.get(key, '')
