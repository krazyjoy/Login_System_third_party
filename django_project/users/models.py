from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from .manager import UserManager
import uuid

class TestUser(AbstractUser):
    class Gender(models.TextChoices):
        FEMALE = 'female', 'Female'
        MALE = 'male', 'Male'

    class RegisterFrom(models.TextChoices):
        DEFAULT = 'default', 'Default'
        FACEBOOK = 'facebook', 'Facebook'
        GOOGLE = 'google', 'Google'
        APPLE = 'apple', 'Apple'
    # username = models.CharField(max_length=150, unique=True, default='')
    username = models.CharField(max_length=150)  # No unique=True
    name = models.CharField(max_length=150, unique=True, default=None)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UUID')
    # uuid =
    register_from = models.CharField(max_length=10, choices=RegisterFrom.choices, default=RegisterFrom.DEFAULT)
    # email is an existed field
    email_verified_at = models.DateTimeField(null=True, blank=True)

    avatar = models.CharField(max_length=200, null=True)

    gender = models.CharField(max_length=10, choices=Gender.choices, default=Gender.MALE)

    birthday = models.DateTimeField(null=True)

    phone = models.CharField(max_length=256, null=True, default=None)

    website = models.CharField(max_length=100, default=None)

    biography = models.TextField(default=None)

    zipcode = models.CharField(max_length=10, null=False, default=None)

    country = models.CharField(max_length=50, null=False, default=None)

    state = models.CharField(max_length=100, null=False, default=None)

    city = models.CharField(max_length=120, null=False, default=None)

    address = models.CharField(max_length=512, null=False, default=None)

    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True)

    following_count = models.IntegerField(default=0)

    follower_count = models.IntegerField(default=0)

    block = models.JSONField(null=True)


    article = models.JSONField(null=True)

    remember_token = models.CharField(max_length=100, null=True, default=None)

    remember_token_expiration = models.DateTimeField(null=True, default=None)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',  # Choose a related_name that does not clash
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',  # Choose a related_name that does not clash
        related_query_name='custom_user'
    )

    # Override the USERNAME_FIELD to use 'name' instead of 'username'
    USERNAME_FIELD = 'name'
    EMAIL_FIELD = 'email'

    # Define any other fields required for authentication
    REQUIRED_FIELDS = ['email']  # Add any other required fields
    objects = UserManager()
    def __str__(self):
        return self.name



