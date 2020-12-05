# Generated by Django 3.0.3 on 2020-12-05 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0009_auto_20201201_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsorganization',
            name='platform_radio',
        ),
        migrations.AddField(
            model_name='newsorganization',
            name='platform_commercial_radio',
            field=models.BooleanField(default=False, help_text='News Organization airs on commercial radio.'),
        ),
        migrations.AddField(
            model_name='newsorganization',
            name='platform_community_radio',
            field=models.BooleanField(default=False, help_text='News Organization airs on community radio.'),
        ),
        migrations.AddField(
            model_name='newsorganization',
            name='platform_public_radio',
            field=models.BooleanField(default=False, help_text='News Organization airs on public radio.'),
        ),
    ]
