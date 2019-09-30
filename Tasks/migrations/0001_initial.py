# Generated by Django 2.2.3 on 2019-09-30 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodingChallenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('due_by', models.DateTimeField()),
                ('completed_status', models.BooleanField(default=False)),
                ('allowed_time', models.DateTimeField()),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_by', models.DateTimeField()),
                ('notest', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('worth', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('notes', models.TextField()),
                ('course', models.ManyToManyField(to='Classes.Course')),
            ],
        ),
    ]
