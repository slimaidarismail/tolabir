# Generated by Django 2.0.2 on 2018-02-25 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tafaha', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='image',
            field=models.ImageField(blank=True, upload_to='img/tafaha/answers'),
        ),
    ]
