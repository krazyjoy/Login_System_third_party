# Generated by Django 5.0.2 on 2024-03-04 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_testuser_remember_token_expiration'),
    ]

    operations = [
        migrations.AddField(
            model_name='testuser',
            name='block',
            field=models.JSONField(null=True),
        ),
    ]
