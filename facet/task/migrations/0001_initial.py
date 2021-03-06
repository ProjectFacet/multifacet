# Generated by Django 3.0.3 on 2020-04-06 23:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('editorial', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Name of the task.')),
                ('text', models.TextField(blank=True, help_text='Content of the task.')),
                ('status', models.CharField(choices=[('Identified', 'Identified'), ('In Progress', 'In Progress'), ('Complete', 'Complete')], help_text='Task status.', max_length=50)),
                ('important', models.BooleanField(default=False, help_text='Whether a task is important.')),
                ('creation_date', models.DateTimeField(auto_now_add=True, help_text='Date and time task is created.')),
                ('due_date', models.DateTimeField(blank=True, help_text='Date and time task is to be completed.')),
                ('inprogress_date', models.DateTimeField(blank=True, help_text='Date and time task status is changed to in progress.', null=True)),
                ('completion_date', models.DateTimeField(auto_now_add=True, help_text='Date and time task status is changed to complete.', null=True)),
                ('anchor', models.OneToOneField(help_text='The anchor object', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_anchor', to='base.Anchor')),
                ('anchor_profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Anchor')),
                ('assigned_to', models.ManyToManyField(blank=True, help_text='The participants assigned to the task.', related_name='taskassignedparticipant', to=settings.AUTH_USER_MODEL)),
                ('entity_owner', models.OneToOneField(help_text='Entity that owns this.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.EntityOwner')),
                ('notes', models.ManyToManyField(blank=True, to='note.Note')),
                ('participant_owner', models.OneToOneField(help_text='Participant who created/owns this.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('simple_audio_assets', models.ManyToManyField(blank=True, to='editorial.SimpleAudio')),
                ('simple_document_assets', models.ManyToManyField(blank=True, to='editorial.SimpleDocument')),
                ('simple_image_assets', models.ManyToManyField(blank=True, to='editorial.SimpleImage')),
                ('simple_video_assets', models.ManyToManyField(blank=True, to='editorial.SimpleVideo')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'ordering': ['name'],
            },
        ),
    ]
