# Generated by Django 4.1.3 on 2022-11-30 08:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_user_address_user_tel_user_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
