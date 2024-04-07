# Generated by Django 5.0.2 on 2024-03-26 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_testuser_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testuser',
            name='address',
            field=models.CharField(default=None, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='biography',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='city',
            field=models.CharField(default=None, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='country',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='state',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='website',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]