# Generated by Django 2.2.4 on 2024-04-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20240417_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discount_date_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
