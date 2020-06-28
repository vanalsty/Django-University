# Generated by Django 3.0.7 on 2020-06-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('courseNumber', models.IntegerField(primary_key='True', serialize=False)),
                ('Title', models.CharField(blank='True', default='', max_length=50, null='False')),
                ('Instructor', models.CharField(blank='True', default='', max_length=50, null='False')),
                ('classDuration', models.FloatField(max_length=30)),
            ],
        ),
    ]