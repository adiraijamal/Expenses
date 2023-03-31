from django import forms
from dailytrans.models import Transactions, MainCategory, SubCategory

class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ('trans_date', 'trans_type', 'trans_main_category', 'trans_sub_category', 'trans_mode', 'trans_amount')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trans_main_category'].queryset = MainCategory.objects.all()
        self.fields['trans_sub_category'].queryset = SubCategory.objects.all()
