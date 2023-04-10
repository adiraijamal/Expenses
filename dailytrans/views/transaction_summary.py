from django.db.models import Case, Sum, Value, When
from django.db.models.functions import TruncMonth
from django.db import models
from django.shortcuts import render
from dailytrans.models import Transactions


def transaction_summary(request):
    cols = [{'name': 'Cash', 'label': 'Cash'}, {'name': 'ENBD', 'label': 'ENBD'}, {'name': 'NoL', 'label': 'NoL'},
            {'name': 'Pay IT', 'label': 'Pay IT'}, {'name': 'SIB', 'label': 'SIB'}]

    totals = Transactions.objects.annotate(
        month=TruncMonth('trans_date')
    ).values(
        'month', 'trans_mode'
    ).annotate(
        tot=Sum('trans_amount'),
        trans_income=Sum(Case(
            When(trans_amount__gt=0, then='trans_amount'),
            default=Value(0),
            output_field=models.DecimalField()
        )),
        trans_expense=Sum(Case(
            When(trans_amount__lt=0, then='trans_amount'),
            default=Value(0),
            output_field=models.DecimalField()
        )),
        balance=Sum('trans_amount'),
    ).order_by()

    total_modes = Transactions.objects.values('trans_mode').annotate(balance=Sum('trans_amount'))

    # Create a dictionary to hold the data
    data = {}

    # Loop through the query results and populate the dictionary
    for row in totals:
        month = row['month'].strftime('%b %Y')
        trans_mode = row['trans_mode']
        if month not in data:
            data[month] = {}
        if trans_mode not in data[month]:
            data[month][trans_mode] = {}
        data[month][trans_mode]['trans_income'] = row['trans_income']
        data[month][trans_mode]['trans_expense'] = row['trans_expense']
        data[month][trans_mode]['balance'] = row['balance']

    # Add the total_modes to the data dictionary
    for rows in total_modes:
        trans_modes = rows['trans_mode']
        if 'Total' not in data:
            data['Total'] = {}
        if trans_modes not in data['Total']:
            data['Total'][trans_modes] = {}
        data['Total'][trans_modes]['balance'] = rows['balance']

    # Pass the dictionary to the template for rendering
    return render(request, 'transaction_summary.html', {'data': data, 'cols': cols, 'total_modes': total_modes})
