# Generated by Django 2.2.11 on 2020-04-06 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0002_newsorganizationnetwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsorganizationnetwork',
            name='members',
            field=models.ManyToManyField(related_name='network_members', to='base.NetworkMember'),
        ),
    ]
