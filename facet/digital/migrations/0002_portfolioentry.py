# Generated by Django 3.0.3 on 2020-12-05 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internalasset', '0002_auto_20201201_1855'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('digital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Title of the portfolio entry', max_length=500)),
                ('link', models.URLField(blank=True, help_text='Link to portfolio item.', max_length=500, null=True)),
                ('date', models.DateTimeField(blank=True, help_text='The publish date of the portfolio entry.')),
                ('public', models.BooleanField(default=True, help_text='whether portfolio entry is shown on public profile.')),
                ('internal_audio', models.ManyToManyField(blank=True, to='internalasset.InternalAudio')),
                ('internal_documents', models.ManyToManyField(blank=True, to='internalasset.InternalDocument')),
                ('internal_images', models.ManyToManyField(blank=True, to='internalasset.InternalImage')),
                ('internal_videos', models.ManyToManyField(blank=True, to='internalasset.InternalVideo')),
                ('participant_owner', models.ForeignKey(help_text='Participant who owns the portfolio entry.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
            },
        ),
    ]
