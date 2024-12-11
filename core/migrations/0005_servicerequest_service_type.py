# Generated by Django 4.2.14 on 2024-08-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_servicerequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='service_type',
            field=models.CharField(choices=[('training', 'Training'), ('consulting', 'Consulting')], max_length=20, null=True),
        ),
    ]