# Generated by Django 3.2.13 on 2022-06-09 03:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20220609_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='new',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
