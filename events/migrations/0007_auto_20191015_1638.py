# Generated by Django 2.2.3 on 2019-10-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20190925_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='people',
        ),
        migrations.AddField(
            model_name='interview',
            name='people',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
