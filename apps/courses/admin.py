# Python modules
from typing import Optional, Sequence

#Django modules
from django.contrib.admin import ModelAdmin, register
from django.core.handlers.wsgi import WSGIRequest

#Project modules
from .models import LessonModule, CourseModule

@register(LessonModule)
class LessonAdmin(ModelAdmin):
    """ Lesson admin configuration class"""
    list_display = (
        'id',
        'course',
        'title',
        'created_at',
    )

    list_display_links = (
        'id',
    )

    list_per_page = 50

    search_fields = (
        'id',
        'title',
    )

    ordering = (
        '-updated_at',
    )

    list_filter = (
        'updated_at',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'deleted_at',
    )

    # filter_horizontal = (
    #     'title',
    # )

    save_on_top = True

    fieldsets = (
        (
            "Lesson Information", {
                "fields": (
                    'course',
                    'title',
                )
            }
        ),(
            "Date and Time Information", {
                "fields": (
                    "created_at",
                    "updated_at",
                    "deleted_at",
                )
            }
        )
    )

    def has_add_permission(self, request: WSGIRequest) -> bool:
        """ Disable add permission """
        return True

    def has_delete_permission(self, request: WSGIRequest, obj: Optional[LessonModule] = None) -> bool:
        """ Disable delete permission """
        return False

    def has_change_permission(self, request: WSGIRequest, obj: Optional[LessonModule] = None) -> bool:
        """ Disable change permission """
        return True

@register(CourseModule)
class CourseAmin(ModelAdmin):
    """ Course Admin panel """
    ...