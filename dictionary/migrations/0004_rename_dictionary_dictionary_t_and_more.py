# Generated by Django 4.0.4 on 2022-04-23 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_dictionary_history_delete_dictionary_t'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='dictionary',
            new_name='dictionary_t',
        ),
        migrations.RenameModel(
            old_name='history',
            new_name='history_t',
        ),
    ]
