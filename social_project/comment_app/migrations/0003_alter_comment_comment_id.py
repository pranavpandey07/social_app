# Generated by Django 4.0.1 on 2022-02-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment_app', '0002_alter_comment_comment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.CharField(auto_created=True, max_length=10000, primary_key=True, serialize=False),
        ),
    ]
