# Generated by Django 4.2.6 on 2023-11-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_data', '0003_webdata_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webdata',
            name='gender',
            field=models.CharField(max_length=20),
        ),
    ]