# Generated by Django 3.0 on 2019-12-13 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_snippet_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='description',
            field=models.TextField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='snippet',
            name='image_url',
            field=models.CharField(default=0, max_length=2083),
        ),
    ]
