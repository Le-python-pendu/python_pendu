# Generated by Django 4.0.4 on 2022-04-26 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_users', '0002_users_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
