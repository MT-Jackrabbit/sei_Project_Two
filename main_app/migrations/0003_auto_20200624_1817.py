# Generated by Django 3.0.7 on 2020-06-24 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200624_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='imageURL',
            field=models.ImageField(blank=True, default='', upload_to='profile_image'),
        ),
    ]