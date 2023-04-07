import calendar
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.db.models import Sum
from dailytrans.models import Transactions
from datetime import datetime, timedelta
from decimal import Decimal
from django.db.models import Sum
from dailytrans.models import Transactions

def calculate_totals(months):
    data = {}

    for month in months:
        # get all transactions for the current month
        transactions = Transactions.objects.filter(trans_date__month=month)

        # create a dictionary to store data for the current month
        data[month] = {}

        # loop through each payment mode and calculate income, expense and balance
        for mode in Transactions.PAYMENT_MODE_CHOICES:
            mode_name = mode[1]
            mode_transactions = transactions.filter(payment_mode=mode[0])
            total_income = mode_transactions.filter(trans_amount__gt=0).aggregate(Sum('trans_amount'))['trans_amount__sum'] or Decimal('0')
            total_expense = mode_transactions.filter(trans_amount__lt=0).aggregate(Sum('trans_amount'))['trans_amount__sum'] or Decimal('0')
            total_balance = total_income + total_expense
            data[month][mode_name] = {
                'total_income': total_income,
                'total_expense': total_expense,
                'total_balance': total_balance,
            }
            # print the data for each transaction mode in the current month
            print(
                f"  Mode: {mode_name}, Total Income: {total_income}, Total Expense: {total_expense}, Total Balance: {total_balance}")

            return data
