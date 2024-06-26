# Generated by Django 5.0.2 on 2024-03-03 19:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('users', '0001_initial'), ('users', '0002_alter_testuser_name')]

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=36, unique=True)),
                ('register_from', models.CharField(choices=[('default', 'Default'), ('facebook', 'Facebook'), ('google', 'Google'), ('apple', 'Apple')], default='default', max_length=10)),
                ('name', models.CharField(default=None, max_length=150, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('email_verified_at', models.DateTimeField(blank=True, null=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('avatar', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], default='male', max_length=10)),
                ('birthday', models.DateTimeField(null=True)),
                ('phone', models.CharField(default=None, max_length=256, null=True)),
                ('website', models.CharField(default=None, max_length=100)),
                ('biography', models.TextField(default=None)),
                ('zipcode', models.CharField(default=None, max_length=10)),
                ('country', models.CharField(default=None, max_length=50)),
                ('state', models.CharField(default=None, max_length=100)),
                ('city', models.CharField(default=None, max_length=120)),
                ('address', models.CharField(default=None, max_length=512)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=11, null=True)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ('following_count', models.IntegerField(default=0)),
                ('follower_count', models.IntegerField(default=0)),
                ('remember_token', models.CharField(default=None, max_length=100, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.IntegerField(default=0)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting account.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=150)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_groups', related_query_name='custom_user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_permissions', related_query_name='custom_user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
