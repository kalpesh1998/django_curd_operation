# Generated by Django 3.0.5 on 2020-04-17 10:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
