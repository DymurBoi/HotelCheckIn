# Generated by Django 5.1.3 on 2024-11-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_roomcategory_room_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomcategory',
            name='room_photo',
            field=models.ImageField(blank=True, default='fallback.png', upload_to='media/'),
        ),
    ]
