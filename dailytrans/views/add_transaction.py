from django.shortcuts import render
from dailytrans.forms import AddTransactionForm
from django.forms import formset_factory


def add_transaction(request):
    AddTransactionFormFormSet = formset_factory(AddTransactionForm, extra=1)
    if request.method == 'POST':
        formset = AddTransactionFormFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                # Save each form
                pass  # replace this with your code
            # redirect to some page after saving all forms
    else:
        formset = AddTransactionFormFormSet()
    context = {'formset': formset}
    print(context)
    return render(request, 'add_transaction.html', context)
