# Generated by Django 3.0.3 on 2020-12-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0002_portfolioentry'),
        ('base', '0005_auto_20200620_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='portfolio',
            field=models.ManyToManyField(blank=True, to='digital.PortfolioEntry'),
        ),
    ]