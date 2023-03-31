from django.shortcuts import render
from django.http import JsonResponse
from django.db.models.functions import TruncMonth
from django.db.models import Sum
from dailytrans.models import Transactions
from django.template.loader import render_to_string


def report_monthly_ajax(request, month):
    month_int = int(month)
    transactions = Transactions.objects.filter(
        trans_date__year=2023, trans_date__month=month_int
    ).annotate(month=TruncMonth('trans_date')).values('month').annotate(
        total=Sum('trans_amount')
    ).values('month', 'total')

    data = {
        'html': render_to_string(
            'report_monthly_ajax.html',
            {'transactions': transactions}
        )
    }
    return JsonResponse(data)
