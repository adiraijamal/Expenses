from django import forms
from django.utils import timezone
from dailytrans.models import Transactions, MainCategory, SubCategory

TRANSACTION_TYPE_CHOICES = [
    ('income', 'Income'),
    ('expense', 'Expense'),
]


PAYMENT_MODE_CHOICES = [
    ('cash', 'Cash'),
    ('enbd', 'ENBD'),
    ('nol', 'NoL'),
    ('payit', 'PayIT'),
    ('sib', 'SIB'),
]


class AddTransactionForm(forms.ModelForm):
    trans_date = forms.DateField(initial=timezone.now().date(), widget=forms.DateInput(attrs={'type': 'date'}))
    trans_type = forms.ChoiceField(choices=Transactions.TRANSACTION_TYPE_CHOICES)
    trans_main_category = forms.ModelChoiceField(queryset=MainCategory.objects.all())
    trans_sub_category = forms.ModelChoiceField(queryset=SubCategory.objects.all())
    trans_mode = forms.ChoiceField(choices=PAYMENT_MODE_CHOICES)
    trans_amount = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Transactions
        fields = '__all__'

    def clean_trans_amount(self):
        trans_type = self.cleaned_data.get('trans_type')
        trans_amount = self.cleaned_data.get('trans_amount')
        if trans_type == 'expense':
            trans_amount = -trans_amount
        return trans_amount

    def clean_trans_mode(self):
        trans_mode = self.cleaned_data.get('trans_mode')
        return trans_mode.lower()
