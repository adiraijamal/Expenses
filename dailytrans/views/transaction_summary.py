import calendar
from django.db.models import Sum
from django.shortcuts import render
from dailytrans.models import Transactions


def transaction_summary(request):
    months = Transactions.objects.values('trans_date__month').distinct()
    data = {}
    running_total = 0
    running_total_modes = {}
    for obj in months:
        month = calendar.month_name[obj['trans_date__month']]
        qs = (
            Transactions.objects
            .filter(trans_date__month=obj['trans_date__month'])
            .order_by('trans_id', 'trans_date')  # Add ordering to ensure correct running total
        )
        total_modes = {}
        for trans in qs:
            running_total += trans.trans_amount
            trans.running_total = running_total
            # Update running total for each trans_mode
            mode_total = running_total_modes.get(trans.trans_mode, 0)
            mode_total += trans.trans_amount
            running_total_modes[trans.trans_mode] = mode_total
            trans.running_total_modes = mode_total
            # Update total modes for this month
            mode_month_total = total_modes.get(trans.trans_mode, 0)
            mode_month_total += trans.trans_amount
            total_modes[trans.trans_mode] = mode_month_total

        amount = qs.aggregate(total=Sum('trans_amount'))

        # Add this month's data to the overall data dictionary
        data[obj['trans_date__month']] = {
            'month': month,
            'qs': qs,
            'total': amount['total'],
            'total_modes': total_modes,
            'running_total': running_total,
            'running_total_modes': running_total_modes.copy()  # Make a copy to avoid modifying the running total dict
        }

    context = {'data': data}

    return render(request, 'test2.html', context)
