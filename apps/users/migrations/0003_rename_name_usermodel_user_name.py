# Generated by Django 5.0.6 on 2024-05-16 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usermodel_delete_postmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='name',
            new_name='user_name',
        ),
    ]
