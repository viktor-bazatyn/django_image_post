# Generated by Django 4.2.4 on 2024-05-08 14:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('djangogramm', '0009_remove_post_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
