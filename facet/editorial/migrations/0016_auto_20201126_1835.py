# Generated by Django 3.0.3 on 2020-11-27 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internalasset', '0001_initial'),
        ('editorial', '0015_audioasset_documentasset_imageasset_videoasset'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='audio_assets',
            field=models.ManyToManyField(blank=True, to='editorial.AudioAsset'),
        ),
        migrations.AddField(
            model_name='item',
            name='document_assets',
            field=models.ManyToManyField(blank=True, to='editorial.DocumentAsset'),
        ),
        migrations.AddField(
            model_name='item',
            name='image_assets',
            field=models.ManyToManyField(blank=True, to='editorial.ImageAsset'),
        ),
        migrations.AddField(
            model_name='item',
            name='video_assets',
            field=models.ManyToManyField(blank=True, to='editorial.VideoAsset'),
        ),
        migrations.AddField(
            model_name='project',
            name='internal_audio_assets',
            field=models.ManyToManyField(blank=True, to='internalasset.InternalAudio'),
        ),
        migrations.AddField(
            model_name='project',
            name='internal_document_assets',
            field=models.ManyToManyField(blank=True, to='internalasset.InternalDocument'),
        ),
        migrations.AddField(
            model_name='project',
            name='internal_image_assets',
            field=models.ManyToManyField(blank=True, to='internalasset.InternalImage'),
        ),
        migrations.AddField(
            model_name='project',
            name='internal_video_assets',
            field=models.ManyToManyField(blank=True, to='internalasset.InternalVideo'),
        ),
        migrations.AddField(
            model_name='story',
            name='internal_audio_assets',
            field=models.ManyToManyField(blank=True, to='internalasset.InternalAudio'),
        ),
        migrations.AddField(
            model_name='story',
            name='internal_document_assets',
            field=models.ManyToManyField(blank=True, to='internalasset.InternalDocument'),
        ),
        migrations.AddField(
            model_name='story',
            name='internal_image_assets',
            field=models.ManyToManyField(blank=True, to='internalasset.InternalImage'),
        ),
        migrations.AddField(
            model_name='story',
            name='internal_video_assets',
            field=models.ManyToManyField(blank=True, to='internalasset.InternalVideo'),
        ),
    ]
