# Generated by Django 5.1.1 on 2024-09-30 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='password1',
            new_name='password',
        ),
    ]
