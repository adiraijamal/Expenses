from datetime import date
from django.db.models import Sum
from dailytrans.models import Transactions

# Define the list of transaction modes
trans_modes = ['Cash', 'ENBD', 'NoL', 'Pay IT', 'SIB']

# Define the list of months to include in the summary
start_date = date(2023, 1, 1)
end_date = date(2023, 4, 30)
months = []
current_month = start_date
while current_month <= end_date:
    months.append(current_month)
    year = current_month.year
    month = current_month.month + 1
    if month > 12:
        year += 1
        month = 1
    current_month = date(year, month, 1)

# Initialize the summary as a list of dictionaries
summary = []
for month in months:
    month_summary = {'month': month.strftime('%B %Y')}
    for mode in trans_modes:
        total_income = Transactions.objects.filter(
            trans_date__year=month.year,
            trans_date__month=month.month,
            trans_mode=mode,
            trans_type='income'
        ).aggregate(Sum('trans_amount'))['trans_amount__sum'] or 0
        print(total_income)
        total_expense = Transactions.objects.filter(
            trans_date__year=month.year,
            trans_date__month=month.month,
            trans_mode=mode,
            trans_type='expense'
        ).aggregate(Sum('trans_amount'))['trans_amount__sum'] or 0
        balance = total_income - total_expense
        month_summary[mode] = {
            'total_income': total_income,
            'total_expense': total_expense,
            'balance': balance
        }
    summary.append(month_summary)

    # Return the summary dictionary
    return render(request, 'test3.html', {'summary': summary})

