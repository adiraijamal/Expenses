from django.shortcuts import render, redirect
from dailytrans.models import Transactions
from dailytrans.forms import AddTransactionForm
from django.contrib import messages
from django.urls import reverse

def add_transaction(request):
    errors = None
    if request.method == 'POST':
        transactions_input = request.POST.get('transactions')
        transactions = transactions_input.split('\n')
        for transaction_str in transactions:
            transaction_fields = transaction_str.strip().split(',')
            form = AddTransactionForm({'trans_date': transaction_fields[0],
                                       'trans_type': transaction_fields[1],
                                       'trans_main_category': transaction_fields[2],
                                       'trans_sub_category': transaction_fields[3],
                                       'trans_mode': transaction_fields[4],
                                       'trans_amount': transaction_fields[5]})
            if form.is_valid():
                transaction = form.save(commit=False)
                if transaction.trans_type == 'Expense':
                    transaction.trans_amount = -abs(transaction.trans_amount)
                transaction.save()
                messages.success(request, 'Transaction added successfully!')
            else:
                errors = form.errors
    else:
        form = AddTransactionForm()

    context = {'form': form, 'errors': errors}
    return render(request, 'add_transaction.html', context)
