# Generated by Django 3.2.7 on 2021-11-15 19:40

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=False, quality=100, size=[1200, 800], upload_to='about'),
        ),
        migrations.AlterField(
            model_name='about',
            name='order',
            field=models.IntegerField(default=439),
        ),
    ]