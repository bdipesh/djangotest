# Generated by Django 2.0.6 on 2019-10-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_usermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
    ]
