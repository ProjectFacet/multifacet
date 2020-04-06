# Generated by Django 3.0.3 on 2020-04-06 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('freelance', '0001_initial'),
        ('entity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsOrganizationSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collaborations', models.BooleanField(default=False, help_text='The organization is using the account for base features of editorial workflow, project management and collaboration.')),
                ('freelance_management', models.BooleanField(default=False, help_text='The organization is using the account to manage contractors.')),
                ('partner_discovery', models.BooleanField(default=True, help_text='Base level subscription. Allows organization to be publicly listed for search as a potential collaborative partner. Allows org users to see other publicly listed orgs.')),
                ('newsorganization', models.OneToOneField(help_text='Organization associated with this subscription if Org subscription type.', on_delete=django.db.models.deletion.CASCADE, to='entity.NewsOrganization')),
            ],
        ),
        migrations.CreateModel(
            name='FreelanceSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freelancer', models.ForeignKey(help_text='Freelancer associated with this subscription.', on_delete=django.db.models.deletion.CASCADE, to='freelance.FreelanceJournalist')),
            ],
        ),
    ]
