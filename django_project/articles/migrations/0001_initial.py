# Generated by Django 5.0.2 on 2024-03-18 19:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UUID')),
                ('api_feed_id', models.BigIntegerField(blank=True, null=True)),
                ('source_name', models.TextField(blank=True, null=True)),
                ('source_uuid', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('context', models.TextField(blank=True, null=True)),
                ('source_url', models.TextField(blank=True, null=True)),
                ('image_url', models.TextField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('published_at', models.TextField(blank=True, null=True)),
                ('symbols', models.TextField(blank=True, null=True)),
                ('sectors', models.FloatField(blank=True, null=True)),
                ('industries', models.FloatField(blank=True, null=True)),
                ('report', models.IntegerField(blank=True, null=True)),
                ('created_at', models.TextField(blank=True, null=True)),
                ('update_at', models.TextField(blank=True, null=True)),
                ('deleted_at', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'articles',
                'managed': False,
            },
        ),
    ]
