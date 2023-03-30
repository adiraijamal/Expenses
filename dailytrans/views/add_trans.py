from django.shortcuts import render, redirect
from dailytrans.forms import AddTransactionForm

def add_trans(request):
    form = AddTransactionForm()
    if request.method == 'POST':
        form = AddTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.save()
            return redirect('success_page')
    return render(request, 'add_trans.html', {'form': form})
