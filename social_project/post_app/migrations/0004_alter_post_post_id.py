# Generated by Django 4.0.1 on 2022-02-02 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0003_alter_post_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
