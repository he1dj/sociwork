# Generated by Django 4.2.7 on 2023-12-11 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("comments", "0002_rename_content_comments_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="parent_id",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="comments.comments"
            ),
        ),
    ]