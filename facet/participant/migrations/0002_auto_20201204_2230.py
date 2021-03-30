# Generated by Django 3.0.3 on 2020-12-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freelancejournalist',
            name='portfolio_link1',
        ),
        migrations.RemoveField(
            model_name='freelancejournalist',
            name='portfolio_link2',
        ),
        migrations.RemoveField(
            model_name='freelancejournalist',
            name='portfolio_link3',
        ),
        migrations.AddField(
            model_name='freelancejournalist',
            name='working_area',
            field=models.TextField(blank=True, help_text='Description of the geographic area the freelancer covers.'),
        ),
        migrations.AddField(
            model_name='freelancemanager',
            name='formats',
            field=models.TextField(blank=True, help_text='Description of formats interested in.'),
        ),
        migrations.AddField(
            model_name='freelancemanager',
            name='topics',
            field=models.TextField(blank=True, help_text='Description of topics interested in.'),
        ),
        migrations.AlterField(
            model_name='freelancejournalist',
            name='availability',
            field=models.TextField(blank=True, help_text='Notes on when freelancer is available or not.'),
        ),
        migrations.AlterField(
            model_name='freelancejournalist',
            name='public',
            field=models.BooleanField(default=True, help_text='Whether the contractor is publicly listed to freelance managers.'),
        ),
        migrations.AlterField(
            model_name='freelancemanager',
            name='public',
            field=models.BooleanField(default=False, help_text='whether the freelance manager is publicly listed'),
        ),
    ]