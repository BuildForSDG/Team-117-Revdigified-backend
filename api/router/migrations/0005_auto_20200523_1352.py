# Generated by Django 3.0.4 on 2020-05-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('router', '0004_auto_20200523_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revdigifieduser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
