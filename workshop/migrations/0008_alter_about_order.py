# Generated by Django 3.2.7 on 2021-11-21 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0007_auto_20211117_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='order',
            field=models.IntegerField(default=730),
        ),
    ]