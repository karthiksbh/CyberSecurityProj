# Generated by Django 3.2.8 on 2022-03-12 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land_details',
            name='land_address',
            field=models.TextField(max_length=500),
        ),
    ]
