# Generated by Django 5.1.2 on 2024-10-23 09:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0008_remove_answer_user_remove_comment_user_answer_token_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="token",
            field=models.CharField(blank=True, editable=False, max_length=64),
        ),
        migrations.AlterField(
            model_name="comment",
            name="token",
            field=models.CharField(blank=True, editable=False, max_length=64),
        ),
    ]