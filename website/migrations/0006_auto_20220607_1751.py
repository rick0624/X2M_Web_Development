# Generated by Django 2.2 on 2022-06-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_new_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]