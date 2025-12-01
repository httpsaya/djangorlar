# Django modules
from django.db.models import (
    ForeignKey,
    CASCADE,
    CharField,
    TextField,
    DecimalField,
)
from decimal import Decimal

# Project modules
from apps.abstracts.models import AbstractBaseModule
from apps.auths.models import CustomUser

class CourseModule(AbstractBaseModule):
    """ Here is my module fields for COURSES"""

    owner = ForeignKey(
        CustomUser,
        on_delete=CASCADE,
        related_name='owned_courses',
    )

    class Meta:
        """ Meta options for Course model"""
        def __str__(self):
            return f"{self.owner}"


class LessonModule(AbstractBaseModule):
    """ Here is my module fields for LESSONS"""

    TITLE_MAX_LENGTH = 255

    course = ForeignKey(
        CourseModule,
        on_delete=CASCADE,
        related_name='lessons',
    )
    title = CharField(
        max_length=TITLE_MAX_LENGTH,
    )
    content = TextField()
    order = DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('0.00'),
    )

    class Meta:
        """ Meta options for Lesson model"""
        def __str__(self):
            return f"{self.title}"


