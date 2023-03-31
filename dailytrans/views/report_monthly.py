from django.shortcuts import render
from dailytrans.models import Transactions

def report_monthly(request, month):
    transactions = Transactions.objects.filter(trans_date__month=month)
    context = {'transactions': transactions, 'month': month}
    return render(request, 'report_monthly.html', context)
