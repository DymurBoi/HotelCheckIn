# Generated by Django 5.1.1 on 2024-11-03 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortingroom', '0011_alter_reservation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sortingroom.room'),
        ),
    ]