# Generated by Django 3.1.2 on 2020-11-05 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0016_auto_20201105_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 5, 17, 48, 18, 446859)),
        ),
    ]
