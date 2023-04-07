from django.core.management.base import BaseCommand
from dailytrans.models import Transactions

class Command(BaseCommand):
    help = 'Calculates totals for transactions'

    def handle(self, *args, **options):
        total = 0
        transactions = Transactions.objects.all()
        for transaction in transactions:
            total += transaction.trans_amount
        print(f'Total: {total}')
