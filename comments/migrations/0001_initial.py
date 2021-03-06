# Generated by Django 3.0.8 on 2021-01-05 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
