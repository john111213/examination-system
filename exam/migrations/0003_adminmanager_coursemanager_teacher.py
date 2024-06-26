# Generated by Django 3.2.19 on 2023-12-27 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_alter_student_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminManager',
            fields=[
                ('sid', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('F', '女'), ('M', '男')], max_length=1, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('pwd', models.CharField(max_length=20, verbose_name='密码')),
            ],
            options={
                'verbose_name': '管理人员',
                'verbose_name_plural': '管理人员信息表',
            },
        ),
        migrations.CreateModel(
            name='courseManager',
            fields=[
                ('sid', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('F', '女'), ('M', '男')], max_length=1, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('pwd', models.CharField(max_length=20, verbose_name='密码')),
            ],
            options={
                'verbose_name': '教务人员',
                'verbose_name_plural': '教务人员信息表',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('sid', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='教师编号')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('F', '女'), ('M', '男')], max_length=1, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('pwd', models.CharField(max_length=20, verbose_name='密码')),
                ('academy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.academy', verbose_name='学院')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.major', verbose_name='专业')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师信息表',
            },
        ),
    ]
