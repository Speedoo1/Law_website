# Generated by Django 4.1.3 on 2022-11-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_practicearea_learnmore'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourpurpose',
            name='littleImg',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ourpurpose',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ourpurpose',
            name='topic',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]