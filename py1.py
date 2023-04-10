import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expenses.settings')
django.setup()

from dailytrans.models import Transactions
import calendar
from django.db.models import Sum


def process_transactions():
    # loop through each month and calculate income, expense and balance for each transaction mode
    for month in months:
        # convert month number to month name
        month_name = calendar.month_name[month]

        # get all transactions for the current month
        transactions = Transactions.objects.filter(trans_date__month=month)

        # create a dictionary to store data for the current month
        data[month_name] = {}

        # loop through each transaction mode and calculate income, expense and balance
        for mode in Transactions.PAYMENT_MODE_CHOICES:
            mode_name = mode[1]
            mode_transactions = transactions.filter(trans_mode=mode[0])
            total_income = mode_transactions.filter(trans_amount__gt=0).aggregate(Sum('trans_amount'))['trans_amount__sum'] or Decimal('0')
            total_expense = mode_transactions.filter(trans_amount__lt=0).aggregate(Sum('trans_amount'))['trans_amount__sum'] or Decimal('0')
            total_balance = total_income + total_expense
            data[month_name][mode_name] = {
                'total_income': total_income,
                'total_expense': total_expense,
                'total_balance': total_balance,
            }

            # print the data for each transaction mode in the current month
            print(f"Month: {month_name}, Mode: {mode_name}, Total Income: {total_income}, Total Expense: {total_expense}, Total Balance: {total_balance}")

# call the process_transactions function to run your code
process_transactions()
