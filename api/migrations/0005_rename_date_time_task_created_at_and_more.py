# Generated by Django 4.2.6 on 2023-10-06 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_created_by_task_name_urls_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date_time',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='Name_Urls',
            new_name='created_by',
        ),
    ]
