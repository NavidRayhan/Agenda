# Generated by Django 2.2.3 on 2019-10-22 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0008_auto_20191022_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codingchallenge',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
