# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-11 02:54
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordpress', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordpress',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
