# Generated by Django 3.1.2 on 2020-11-05 14:46

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0015_auto_20201105_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 5, 17, 46, 58, 366041)),
        ),
    ]
