# Generated by Django 5.0.2 on 2024-03-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_testuser_address_alter_testuser_biography_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testuser',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=512),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='article',
            field=models.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='avatar',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='biography',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='birthday',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='block',
            field=models.JSONField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='country',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=8, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=8, default=None, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='remember_token',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='remember_token_expiration',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='website',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='zipcode',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
