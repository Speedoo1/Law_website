# Generated by Django 4.1.3 on 2022-12-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_remove_question_id_question_question_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_id',
        ),
        migrations.AddField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
