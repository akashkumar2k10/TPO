# Generated by Django 2.2.1 on 2019-06-01 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20190601_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sem',
            field=models.PositiveIntegerField(choices=[('6', '6'), ('1', '1'), ('5', '5'), ('7', '7'), ('8', '8'), ('4', '4'), ('', 'select'), ('2', '2'), ('3', '3')], default=5, verbose_name='Semesert'),
        ),
    ]
