from django import forms
from dailytrans.models import Transactions

class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ('trans_date', 'trans_type', 'trans_main_category', 'trans_sub_category', 'trans_mode', 'trans_amount')
        widgets = {
            'trans_date': forms.DateInput(attrs={'type': 'date'}),
        }
