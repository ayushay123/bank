# Generated by Django 4.2.14 on 2024-08-06 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_userbankaccount_is_active_user_disabled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='disabled',
        ),
    ]
