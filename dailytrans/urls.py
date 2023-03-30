from django.urls import path
from .views import index, report_monthwise, add_trans

app_name = 'dailytrans'

urlpatterns = [
    path('', index, name='index'),
    path('report_monthwise/', report_monthwise, name='report_monthwise'),
    path('add_trans/', add_trans, name='add_trans'),
]
