# Generated by Django 4.1.7 on 2023-04-10 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('main_id', models.AutoField(primary_key=True, serialize=False)),
                ('main_name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Main Category',
                'verbose_name_plural': 'Main Categories',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('subcategory_id', models.AutoField(primary_key=True, serialize=False)),
                ('subcategory_name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Sub Category',
                'verbose_name_plural': 'Sub Categories',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('trans_id', models.AutoField(primary_key=True, serialize=False)),
                ('trans_date', models.DateField(db_index=True, verbose_name='Date')),
                ('trans_type', models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=10, verbose_name='Type')),
                ('trans_mode', models.CharField(choices=[('cash', 'Cash'), ('enbd', 'ENBD'), ('nol', 'NoL'), ('payit', 'PayIT'), ('sib', 'SIB')], db_index=True, max_length=10, verbose_name='Payment Mode')),
                ('trans_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('trans_main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='dailytrans.maincategory', verbose_name='Main Category')),
                ('trans_sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='dailytrans.subcategory', verbose_name='Sub Category')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
    ]
