# Django modules
from typing import Any
from django.contrib.messages.context_processors import messages
from django.db.models import (
    EmailField,
    CharField,
    BooleanField,
    DateField,
    DecimalField,
    DateTimeField,
)
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ValidationError

# Project modules
from apps.abstracts.models import AbstractBaseModule

# Password validators
from apps.auths.validators import validate_email_domain, validate_email_payload_not_in_full_name

class CustomUserManager(BaseUserManager):
    """Custom User Manager to make database requests."""
    def __obtain_user_instance(
            self,
            email: str,
            password: str,
            full_name: str,
            **kwargs: dict[str, Any],
    ) -> 'CustomUser':
        """Get user instance."""
        if not email:
            raise ValidationError(
                message="Email field is required", code="email_empty"
            )
        if not full_name:
            raise ValidationError(
                message="Full name name is required.", code='full_name_empty'
            )
        new_user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            password=password,
            **kwargs,
        )
        return new_user


    def create_user(
            self,
            password: str,
            full_name: str,
            email: str,
            **kwargs: dict[str, Any],
    ) -> 'CustomUser':
        """Create Custom user. TODO where is this used?"""

        new_user: 'CustomUser' = self.__obtain_user_instance(
            email=email,
            full_name=full_name,
            password=password,
            **kwargs,
        )
        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user

    def create_superuser(
            self,
            password: str,
            full_name: str,
            email: str,
            **kwargs: dict[str, Any],
    ) -> 'CustomUser':
        """
        Create super user. Used by manage.py createsuperuser.
        """
        new_user: 'CustomUser' = self.__obtain_user_instance(
            email=email,
            password=password,
            full_name=full_name,
            is_staff=True,
            is_superuser=True,
            **kwargs,
        )
        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user


class CustomUser(AbstractBaseUser, PermissionsMixin, AbstractBaseModule):
    """
    Custom user model extending AbstractBaseModule
    """
    EMAIL_MAX_LENGTH = 150
    FULL_NAME_MAX_LENGTH = 150
    PASSWORD_MAX_LENGTH = 254
    PHONE_MAX_LENGTH = 150
    CITY_MAX_LENGTH = 254
    DEPARTMENT_MAX_LENGTH = 254
    SLARY_MAX_LENGTH = 12

    ROLE_CHOICES = [
        ('admin', "Admin"),
        ('manager', "Manager"),
        ('employee', 'Employee'),
    ]

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


    """ Added fields """
    first_name = CharField(
        max_length=FULL_NAME_MAX_LENGTH,
        verbose_name='First name',
    )
    last_name = CharField(
        max_length=FULL_NAME_MAX_LENGTH,
        verbose_name='Last name',
    )
    phone = CharField(
        max_length=PHONE_MAX_LENGTH,
        verbose_name="User's Phone number"
    )
    city = CharField(
        max_length=CITY_MAX_LENGTH,
        verbose_name="City"
    )
    country = CharField(
        max_length=CITY_MAX_LENGTH,
        verbose_name="Country"
    )
    department = CharField(
        max_length=DEPARTMENT_MAX_LENGTH,
        verbose_name="Department",
    )
    role = CharField(
        max_length=DEPARTMENT_MAX_LENGTH,
        choices=ROLE_CHOICES,
        default='employee',
        verbose_name="Role",
    )
    birth_date = DateField(
        null=True,
        blank=True,
        verbose_name="Birth Date",
    )
    salary = DecimalField(
        max_digits=SLARY_MAX_LENGTH,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Salary of User",
    )
    date_joined = DateTimeField(
        auto_now_add=True,
        verbose_name="Joined Date",
    )
    last_login = DateTimeField(
        blank=True,
        null=True,
        verbose_name="Last Login"
    )

    REQUIRED_FIELDS = ["full_name"]
    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    class Meta:
        """ Meta options for CustomUser model"""

        verbose_name='Custom User'
        verbose_name_plural="Custom Users"
        ordering = ["created_at"]

    def clean(self) -> None:
        """Validate the model instance before saving."""
        validate_email_payload_not_in_full_name(
            email=self.email,
            full_name=self.full_name,
        )
        return super().clean()
