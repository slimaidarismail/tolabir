# Generated by Django 2.0.2 on 2018-02-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tafaha', '0003_auto_20180227_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
