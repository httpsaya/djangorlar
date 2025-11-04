# Python modules

# Django modules
from django.db.models import (
    EmailField,
    CharField,
    BooleanField,

)
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Project modules
from apps.abstracts.models import AbstractBaseModule
from apps.auths.validators import validate_email_domain
# Password validators
# from django.contrib.auth.validators import

class CustomUser(AbstractBaseUser, PermissionsMixin, AbstractBaseModule):
    """
    Custom user model extending AbstractBaseModule
    """
    EMAIL_MAX_LENGTH = 150
    FULL_NAME_MAX_LENGTH = 150
    PASSWORD_MAX_LENGTH = 254

    email = EmailField(
        unique=True,
        max_length=EMAIL_MAX_LENGTH,
        db_index=True,
        validators=[validate_email_domain],
        verbose_name='Email address',
        help_text="User's email address",
    )
    full_name = CharField(
        max_length=FULL_NAME_MAX_LENGTH,
        verbose_name='Full name',

    )
    password = CharField(
        max_length=PASSWORD_MAX_LENGTH,
        verbose_name="Password",
        help_text="User's hash representation of password",
    )
    is_staff = BooleanField(
        default=True,
        verbose_name="Active status",
    )
    is_active = BooleanField(
        default=True,
        verbose_name="Active status",
    )

    REQUIRED_FIELDS = ["full_name"]
    USERNAME_FIELD = "email"

    class Meta:
        """ Meta options for CustomUser model"""

        verbose_name='Custom User',
        verbose_name_plural="Custom Users",
        ordering = ["created_at"]