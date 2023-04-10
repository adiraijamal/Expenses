from django.db import models

# Create your models here.


class MainCategory(models.Model):
    main_id = models.AutoField(primary_key=True)
    main_name = models.CharField(max_length=25)

    def __str__(self):
        return self.main_name

    class Meta:
        verbose_name = "Main Category"
        verbose_name_plural = "Main Categories"

    objects = models.Manager()


class SubCategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    subcategory_name = models.CharField(max_length=25)

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

    objects = models.Manager()


class Transactions(models.Model):
    TRANSACTION_TYPE_CHOICES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    PAYMENT_MODE_CHOICES = (
        ('cash', 'Cash'),
        ('enbd', 'ENBD'),
        ('nol', 'NoL'),
        ('payit', 'PayIT'),
        ('sib', 'SIB'),
    )

    trans_id = models.AutoField(primary_key=True)
    trans_date = models.DateField(verbose_name="Date", db_index=True)
    trans_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES, verbose_name="Type")
    trans_main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, verbose_name="Main Category",
                                            related_name="transactions")
    trans_sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name="Sub Category",
                                           related_name="transactions")
    trans_mode = models.CharField(max_length=10, choices=PAYMENT_MODE_CHOICES, verbose_name="Payment Mode",
                                  db_index=True)
    trans_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Amount")

    objects = models.Manager()

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        amount_str = "${:,.2f}".format(self.trans_amount)
        if self.trans_type == 'expense':
            amount_str = "-{}".format(amount_str)

        return (
            f"Transaction ID: {self.trans_id}\n"
            f"Date: {self.trans_date}\n"
            f"Type: {self.trans_type}\n"
            f"Main Category: {self.trans_main_category}\n"
            f"Sub Category: {self.trans_sub_category}\n"
            f"Payment Mode: {self.trans_mode}\n"
            f"Amount: {amount_str}"
        )
