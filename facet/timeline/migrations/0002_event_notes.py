# Generated by Django 2.2.11 on 2020-04-06 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='notes',
            field=models.ManyToManyField(blank=True, to='note.Note'),
        ),
    ]
