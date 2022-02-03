# Generated by Django 4.0.1 on 2022-02-02 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0004_alter_post_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dislikes_count',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes_counts',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='shares_count',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
