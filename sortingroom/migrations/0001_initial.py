# Generated by Django 5.1.1 on 2024-09-30 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_photo', models.ImageField(blank=True, null=True, upload_to='room_photos/')),
                ('room_type', models.CharField(max_length=30)),
                ('room_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]