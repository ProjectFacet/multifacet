# Generated by Django 2.2.11 on 2020-04-06 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_participant_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='anchor_profile',
        ),
    ]