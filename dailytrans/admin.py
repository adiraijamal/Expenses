from django.contrib import admin
from dailytrans.models import Transactions, MainCategory, SubCategory
# Register your models here.


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    pass


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    pass
