# Generated by Django 3.0 on 2019-12-13 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20191213_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='image_url',
        ),
    ]
