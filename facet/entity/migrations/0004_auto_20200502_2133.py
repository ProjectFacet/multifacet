# Generated by Django 3.0.3 on 2020-05-03 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200406_1650'),
        ('entity', '0003_auto_20200502_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsorganizationnetwork',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='network_members', to='base.NetworkMember'),
        ),
    ]
