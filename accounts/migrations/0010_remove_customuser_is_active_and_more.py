# Generated by Django 5.1.3 on 2024-12-05 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_customuser_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_superuser',
        ),
    ]