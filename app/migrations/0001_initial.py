# Generated by Django 3.2.8 on 2022-03-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Land_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_address', models.CharField(max_length=500)),
                ('previous_buyer', models.CharField(default='Government', max_length=250)),
                ('new_buyer', models.CharField(max_length=250)),
                ('hash_pass', models.CharField(max_length=250)),
                ('id_unique', models.CharField(max_length=100)),
                ('date_sale', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]