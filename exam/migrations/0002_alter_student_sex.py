# Generated by Django 3.2.19 on 2023-12-27 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('F', '女'), ('M', '男')], max_length=1, verbose_name='性别'),
        ),
    ]
