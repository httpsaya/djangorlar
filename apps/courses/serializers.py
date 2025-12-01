# Django Rest Framework Modules
from rest_framework.serializers import Serializer

# Project Modules
from .models import CourseModule, LessonModule

class CourseSerializer(Serializer):
    """
    Implementing Course Serializers
    """
    class Meta:
        model = CourseModule

        fields = [
            'id',
            'owner',
        ]
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']


class LessonSerializer(Serializer):
    """
    Implementing Lesson Serializer
    """
    class Meta:
        model = LessonModule

        fields=[
            'id',
            'course',
            'title',
            'content',
            'order',
        ]