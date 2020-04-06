# Generated by Django 2.2.11 on 2020-04-06 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20200405_1926'),
        ('editorial', '0006_audioasset_documentasset_imageasset_simpleaudio_simpledocument_simpleimage_simplevideo_videoasset'),
        ('pickup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storypickupdetail',
            name='partner',
            field=models.OneToOneField(help_text='Partner picking up the story.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Partner'),
        ),
        migrations.CreateModel(
            name='VideoPickupDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_entity_owner_name', models.CharField(help_text='Name of original entity.', max_length=300)),
                ('original_videoasset_name', models.CharField(help_text='Title of original video.', max_length=300)),
                ('partner_name', models.CharField(help_text='Name of partner.', max_length=300)),
                ('pickup_date', models.DateTimeField(auto_now_add=True, help_text='Datetime when pickup was made.')),
                ('original_entity_owner', models.OneToOneField(help_text='Entity that originally made the video available.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.EntityOwner')),
                ('original_videoasset', models.ForeignKey(help_text='Original instance of the videoasset', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='original_videoasset_detail', to='editorial.VideoAsset')),
                ('partner', models.OneToOneField(help_text='Partner picking up the story.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Partner')),
                ('partner_videoasset', models.ForeignKey(help_text='The copied version of the videoasset saved by the partner organization.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videoasset_pickup', to='editorial.VideoAsset')),
            ],
        ),
        migrations.CreateModel(
            name='ImagePickupDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_entity_owner_name', models.CharField(help_text='Name of original entity.', max_length=300)),
                ('original_imageasset_name', models.CharField(help_text='Title of original image.', max_length=300)),
                ('partner_name', models.CharField(help_text='Name of partner.', max_length=300)),
                ('pickup_date', models.DateTimeField(auto_now_add=True, help_text='Datetime when pickup was made.')),
                ('original_entity_owner', models.OneToOneField(help_text='Entity that originally made the image available.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.EntityOwner')),
                ('original_imageasset', models.ForeignKey(help_text='Original instance of the imageasset', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='original_imageasset_detail', to='editorial.ImageAsset')),
                ('partner', models.OneToOneField(help_text='Partner picking up the story.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Partner')),
                ('partner_imageasset', models.ForeignKey(help_text='The copied version of the imageasset saved by the partner organization.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='imageasset_pickup', to='editorial.ImageAsset')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentPickupDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_entity_owner_name', models.CharField(help_text='Name of original entity.', max_length=300)),
                ('original_documentasset_name', models.CharField(help_text='Title of original document.', max_length=300)),
                ('partner_name', models.CharField(help_text='Name of partner.', max_length=300)),
                ('pickup_date', models.DateTimeField(auto_now_add=True, help_text='Datetime when pickup was made.')),
                ('original_documentasset', models.ForeignKey(help_text='Original instance of the documentasset', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='original_documentasset_detail', to='editorial.DocumentAsset')),
                ('original_entity_owner', models.OneToOneField(help_text='Entity that originally made the document available.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.EntityOwner')),
                ('partner', models.OneToOneField(help_text='Partner picking up the story.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Partner')),
                ('partner_documentasset', models.ForeignKey(help_text='The copied version of the documentasset saved by the partner organization.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documentasset_pickup', to='editorial.DocumentAsset')),
            ],
        ),
        migrations.CreateModel(
            name='AudioPickupDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_entity_owner_name', models.CharField(help_text='Name of original entity.', max_length=300)),
                ('original_audioasset_name', models.CharField(help_text='Title of original audio.', max_length=300)),
                ('partner_name', models.CharField(help_text='Name of partner.', max_length=300)),
                ('pickup_date', models.DateTimeField(auto_now_add=True, help_text='Datetime when pickup was made.')),
                ('original_audioasset', models.ForeignKey(help_text='Original instance of the audioasset', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='original_audioasset_detail', to='editorial.AudioAsset')),
                ('original_entity_owner', models.OneToOneField(help_text='Entity that originally made the audio available.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.EntityOwner')),
                ('partner', models.OneToOneField(help_text='Partner picking up the story.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Partner')),
                ('partner_audioasset', models.ForeignKey(help_text='The copied version of the audioasset saved by the partner organization.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audioasset_pickup', to='editorial.AudioAsset')),
            ],
        ),
    ]
