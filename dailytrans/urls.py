from django.urls import path
from dailytrans.views import index, add_transaction, report_monthwise, report_monthly_ajax

app_name = 'dailytrans'

urlpatterns = [
    path('', index, name='index'),
    path('report_monthwise/', report_monthwise, name='report_monthwise' ),
    path('report_monthly_ajax/<int:month>/', report_monthly_ajax, name='report_monthly_ajax'),
    path('add_transaction/', add_transaction, name='add_transaction'),
]
