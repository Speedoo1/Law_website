# Generated by Django 4.1.3 on 2022-11-30 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_question_collapseone_question_collapse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='collapse',
        ),
    ]