from django.shortcuts import render
from django.http import JsonResponse
from dailytrans.models import Transactions

def report_monthly_ajax(request, month):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        transactions = Transactions.objects.filter(trans_date__month=month)
        data = list(transactions.values())
        return JsonResponse(data, safe=False)
    else:
        return render(request, 'report_monthly.html')
