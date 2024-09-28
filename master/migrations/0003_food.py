# Generated by Django 3.2 on 2021-04-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_alter_cruise_year_of_built'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Food_name', models.CharField(max_length=100)),
                ('Food_type', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('Quantity', models.IntegerField()),
                ('Description', models.TextField(max_length=300)),
                ('Food_image', models.ImageField(upload_to='media/images')),
            ],
        ),
    ]
