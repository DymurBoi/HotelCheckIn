# Generated by Django 5.1.1 on 2024-11-16 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_alter_roomcategory_room_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomcategory',
            name='room_photo',
            field=models.ImageField(blank=True, default='lizard.jpeg', null=True, upload_to=''),
        ),
    ]
