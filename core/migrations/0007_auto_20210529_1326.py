# Generated by Django 3.1.4 on 2021-05-29 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210529_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='subscribed',
            field=models.BooleanField(default=True),
        ),
    ]
