# Generated by Django 2.2.4 on 2024-04-17 16:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_productinformation_additional_field3'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount_date_time',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
