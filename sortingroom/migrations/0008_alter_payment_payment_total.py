# Generated by Django 5.1.1 on 2024-11-01 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortingroom', '0007_payment_payment_method_payment_payment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_total',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
    ]
