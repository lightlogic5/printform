# Generated by Django 2.1.4 on 2019-01-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printers', '0003_prints_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prints',
            name='SN',
            field=models.CharField(default=0, max_length=50, verbose_name='打印机编码'),
        ),
    ]
