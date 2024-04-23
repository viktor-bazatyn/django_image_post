# Generated by Django 4.2.4 on 2024-04-23 19:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangogramm", "0006_alter_comment_text_alter_post_comments_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
