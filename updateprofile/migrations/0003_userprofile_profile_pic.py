# Generated by Django 5.1.1 on 2024-10-14 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updateprofile', '0002_userprofile_email_userprofile_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_profile.jpg', upload_to=''),
        ),
    ]