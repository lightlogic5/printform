# Generated by Django 2.1.4 on 2019-01-11 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printers', '0002_prints_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='prints',
            name='state',
            field=models.CharField(choices=[('1', '在使用'), ('2', '报废')], default=1, max_length=1, verbose_name='打印机状态'),
        ),
    ]
