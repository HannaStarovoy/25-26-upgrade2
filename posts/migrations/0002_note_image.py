# Generated by Django 5.0 on 2024-01-12 22:46

import posts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='image',
            field=models.FileField(null=True, upload_to=posts.models.upload_to),
        ),
    ]