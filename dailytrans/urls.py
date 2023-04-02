from django.urls import path
from dailytrans.views import index, add_transaction, report_monthwise

app_name = 'dailytrans'

urlpatterns = [
    path('', index, name='index'),
    path('report_monthwise/', report_monthwise, name='report_monthwise'),
    path('add_transaction/', add_transaction, name='add_transaction'),
]
