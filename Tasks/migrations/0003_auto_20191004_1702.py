# Generated by Django 2.2.3 on 2019-10-04 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0002_auto_20190930_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repeating', models.BooleanField(default=False)),
                ('days', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='codingchallenge',
            name='allowed_time',
            field=models.TimeField(),
        ),
    ]