# Generated by Django 4.0.1 on 2022-02-02 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.PositiveIntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
