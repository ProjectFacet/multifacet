# Generated by Django 3.0.3 on 2020-12-05 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_auto_20201126_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='internal_audio_assets',
            new_name='internal_audio',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='internal_document_assets',
            new_name='internal_documents',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='internal_image_assets',
            new_name='internal_images',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='internal_video_assets',
            new_name='internal_videos',
        ),
    ]
