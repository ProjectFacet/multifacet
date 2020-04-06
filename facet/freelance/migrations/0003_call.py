# Generated by Django 2.2.11 on 2020-04-06 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editorial', '0006_audioasset_documentasset_imageasset_simpleaudio_simpledocument_simpleimage_simplevideo_videoasset'),
        ('entity', '0003_auto_20200405_1926'),
        ('freelance', '0002_freelanceinvoice_freelanceraffiliationrecord_organizationaffiliationrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Title of the call.', max_length=50)),
                ('text', models.TextField(help_text='Text of the call.')),
                ('creation_date', models.DateTimeField(auto_now_add=True, help_text='Day/Time call was created.')),
                ('expiration_date', models.DateTimeField(blank=True, help_text='Day/Time call ends.', null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Is this call active?')),
                ('urgent', models.BooleanField(default=False, help_text='Is this call urgent?')),
                ('timeframe', models.CharField(blank=True, help_text='What is the timeframe for responses?', max_length=100, null=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Active', 'Active'), ('Complete', 'Complete')], help_text='Pitch status choice.', max_length=25)),
                ('organization', models.ForeignKey(help_text='Organization that is making this call.', on_delete=django.db.models.deletion.CASCADE, to='entity.NewsOrganization')),
                ('owner', models.ForeignKey(help_text='Freelance Manager that owns this call.', on_delete=django.db.models.deletion.CASCADE, to='freelance.FreelanceManager')),
                ('simple_audio_assets', models.ManyToManyField(blank=True, to='editorial.SimpleAudio')),
                ('simple_document_assets', models.ManyToManyField(blank=True, to='editorial.SimpleDocument')),
                ('simple_image_assets', models.ManyToManyField(blank=True, to='editorial.SimpleImage')),
                ('simple_video_assets', models.ManyToManyField(blank=True, to='editorial.SimpleVideo')),
                ('tags', models.ManyToManyField(blank=True, to='editorial.Tag')),
            ],
            options={
                'verbose_name': 'Call for Pitch',
                'verbose_name_plural': 'Calls for Pitch',
            },
        ),
    ]
