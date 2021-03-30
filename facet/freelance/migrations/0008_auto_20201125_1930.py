# Generated by Django 3.0.3 on 2020-11-26 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0001_initial'),
        ('entity', '0006_auto_20200611_0950'),
        ('freelance', '0007_auto_20201125_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='editor',
            field=models.ForeignKey(help_text='Editor responsible for this assignment.', null=True, on_delete=django.db.models.deletion.CASCADE, to='participant.FreelanceManager'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='freelancer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='participant.FreelanceJournalist'),
        ),
        migrations.AddField(
            model_name='call',
            name='owner',
            field=models.ForeignKey(help_text='Freelance Manager that owns this call.', null=True, on_delete=django.db.models.deletion.CASCADE, to='participant.FreelanceManager'),
        ),
        migrations.AddField(
            model_name='freelanceinvoice',
            name='freelancer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='participant.FreelanceJournalist'),
        ),
        migrations.AddField(
            model_name='freelanceinvoice',
            name='manager',
            field=models.ForeignKey(help_text='Manager responsible for this assignment.', null=True, on_delete=django.db.models.deletion.CASCADE, to='participant.FreelanceManager'),
        ),
        migrations.AddField(
            model_name='freelanceraffiliationrecord',
            name='freelancer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='participant.FreelanceJournalist'),
        ),
        migrations.AddField(
            model_name='organizationaffiliationrecord',
            name='contacts',
            field=models.ManyToManyField(blank=True, help_text='News Organization Freelance Managers freelancer works with.', related_name='affilation_contact', to='participant.FreelanceManager'),
        ),
        migrations.AddField(
            model_name='organizationaffiliationrecord',
            name='freelancer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='participant.FreelanceJournalist'),
        ),
        migrations.AddField(
            model_name='pitch',
            name='freelancer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='participant.FreelanceJournalist'),
        ),
        migrations.AddField(
            model_name='pitch',
            name='recipient',
            field=models.ForeignKey(blank=True, help_text='Freelance Manager being pitched.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='participant.FreelanceManager'),
        ),
        migrations.AlterUniqueTogether(
            name='freelanceraffiliationrecord',
            unique_together={('organization', 'freelancer')},
        ),
        migrations.AlterUniqueTogether(
            name='organizationaffiliationrecord',
            unique_together={('organization', 'freelancer')},
        ),
    ]