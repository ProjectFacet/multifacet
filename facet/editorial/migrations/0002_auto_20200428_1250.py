# Generated by Django 2.2.11 on 2020-04-28 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editorial', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='collaborate_with',
            new_name='partner_with',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='collaborate_with',
            new_name='partner_with',
        ),
    ]
