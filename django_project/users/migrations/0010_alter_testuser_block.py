# Generated by Django 5.0.2 on 2024-03-26 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_testuser_address_alter_testuser_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testuser',
            name='block',
            field=models.JSONField(blank=True, default=None, null=True),
        ),
    ]
