# Generated by Django 2.2.3 on 2019-09-25 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_interview_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
