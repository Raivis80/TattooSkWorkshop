# Generated by Django 3.2.7 on 2021-11-17 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0006_alter_about_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=254)),
                ('lang', models.CharField(default='en', max_length=2)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='order',
            field=models.IntegerField(default=991),
        ),
    ]
