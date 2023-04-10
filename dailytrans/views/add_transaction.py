from django.shortcuts import render
from dailytrans.forms import AddTransactionForm
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required

@login_required
def add_transaction(request):
    add_transaction_form_form_set = formset_factory(AddTransactionForm, extra=1)
    if request.method == 'POST':
        formset = add_transaction_form_form_set(request.POST)
        if formset.is_valid():
            for form in formset:
                transaction = form.save(commit=False)
                transaction.user = request.user
                transaction.save()
            # redirect to some page after saving all forms
    else:
        formset = add_transaction_form_form_set()
    context = {'formset': formset}

    return render(request, 'add_transaction.html', context)
