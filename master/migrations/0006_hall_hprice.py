# Generated by Django 3.1.7 on 2021-05-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0005_auto_20210505_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='HPrice',
            field=models.IntegerField(default=100),
        ),
    ]
