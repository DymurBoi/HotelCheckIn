# Generated by Django 5.1.1 on 2024-10-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customuser_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
    ]
