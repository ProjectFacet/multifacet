# Generated by Django 3.0.3 on 2020-06-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200406_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='photo',
            field=models.ImageField(blank=True, upload_to='participants'),
        ),
    ]
