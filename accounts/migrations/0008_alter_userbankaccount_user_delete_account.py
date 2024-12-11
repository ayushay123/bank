# Generated by Django 5.0.4 on 2024-07-06 19:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_account_delete_customcaptchastore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankaccount',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
