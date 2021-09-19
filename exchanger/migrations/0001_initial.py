# Generated by Django 3.2.7 on 2021-09-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchanger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(verbose_name='Курс валюты')),
                ('amount', models.FloatField(verbose_name='Сумма')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
        ),
    ]
