from django.shortcuts import render
from django.db.models import Min, Sum
import calendar
from dailytrans.models import Transactions


def report_monthwise(request):
    months = Transactions.objects.values('trans_date__month').distinct()
    data = {}
    for obj in months:
        month = calendar.month_name[obj['trans_date__month']]
        qs = (
            Transactions.objects
            .filter(trans_date__month=obj['trans_date__month'])
        )
        amount = qs.aggregate(total=Sum('trans_amount'))

        data[obj['trans_date__month']] = {
            'month': month,
            'qs': qs,
            'total': amount['total']
        }

    context = {'data': data}
    return render(request, 'report_monthwise.html', context)
