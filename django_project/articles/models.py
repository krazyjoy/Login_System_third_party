# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid

class Articles(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UUID')
    api_feed_id = models.BigIntegerField(blank=True, null=True)
    source_name = models.TextField(blank=True, null=True)
    source_uuid = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    source_url = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    published_at = models.TextField(blank=True, null=True)
    symbols = models.TextField(blank=True, null=True)
    sectors = models.FloatField(blank=True, null=True)
    industries = models.FloatField(blank=True, null=True)
    report = models.IntegerField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    update_at = models.TextField(blank=True, null=True)
    deleted_at = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles'
