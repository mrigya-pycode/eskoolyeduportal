# Generated by Django 3.0.6 on 2020-07-05 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comapp', '0004_accountinfo_expenseinfo_incomeinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Expenseinfo',
        ),
        migrations.DeleteModel(
            name='Incomeinfo',
        ),
    ]
