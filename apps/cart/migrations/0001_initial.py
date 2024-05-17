# Generated by Django 5.0.1 on 2024-05-17 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
        ('users', '0003_rename_name_usermodel_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(db_index=True, verbose_name='Quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.itemmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usermodel')),
            ],
            options={
                'db_table': 'Cart',
            },
        ),
    ]
