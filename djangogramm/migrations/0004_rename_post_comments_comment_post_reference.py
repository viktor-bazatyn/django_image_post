# Generated by Django 4.2.4 on 2024-04-20 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("djangogramm", "0003_rename_post_comment_post_comments_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="post_comments",
            new_name="post_reference",
        ),
    ]
