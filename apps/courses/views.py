# Django Modules
from django.utils import timezone
from django.db.models import Count, QuerySet, Min

# Django Rest Framework Modules
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request as DRFRequest
from rest_framework.response import Response as DRFResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_403_FORBIDDEN,
    HTTP_204_NO_CONTENT,
)

# Python Modules
from typing import Any

# Project Modules
from apps.courses.models import CourseModule, LessonModule
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ViewSet):
    """
    Implementing Course Endpoints
    """
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        """ Optimized Queryset which have:
                - author
                - prefetch_related
                - select_related
                - annotate (likes_count and comments_count)
        """
        return (
            CourseModule.objects
            .filter(deleted_at__isnull=True)
            .select_related('owner')
            .annotate(
                users_count=Count('users', distinct=True)
            )
        )


    def list(
            self,
            request: DRFRequest,
            *args: tuple[Any, ...],
            **kwargs: dict[str, Any],
    ) -> DRFResponse:
        """ Creating GET endpoint"""

        all_courses: QuerySet[CourseModule] = self.get_queryset().all()

        serializer: CourseSerializer = CourseSerializer(
            all_courses,
            many=True,
        )
        return DRFResponse(
            data=serializer.data,
            status=HTTP_200_OK,
        )


    def create(
            self,
            request: DRFRequest,
            *args: tuple[Any, ...],
            **kwargs: dict[str, Any],
    ) -> DRFResponse:
        """
        Implementing Post endpoint for Courses
        """
        serializer: CourseSerializer = CourseSerializer(data=request.data)

        if not serializer.is_valid():
            return DRFResponse(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )

        course = serializer.save(owner=request.user, deleted_at=None)

        return DRFResponse(
            data=serializer.data,
            status=HTTP_201_CREATED,
        )


    def retrieve(
            self,
            request: DRFRequest,
            *args: tuple[Any, ...],
            **kwargs: dict[str, Any],
    ) -> DRFResponse:
        """
        Retrieve single course
        """
        pk = kwargs.get('pk')

        try:
            course = self.get_queryset().get(pk=pk)
        except CourseModule.DoesNotExist:
            return DRFResponse(
                {'detail': 'Not Found'},
                status=HTTP_404_NOT_FOUND
            )
        serializer: CourseSerializer = CourseSerializer(course)

        return DRFResponse(
            serializer.data,
            status=HTTP_200_OK
        )


    def update(
            self,
            request: DRFRequest,
            *args: tuple[Any, ...],
            **kwargs: dict[str, Any],
    ) -> DRFResponse:
        """
        Full update of the course
        """
        pk = kwargs.get('pk')

        try:
            course = self.get_queryset().get(pk=pk)
        except CourseModule.DoesNotExist:
            return DRFResponse(
                {'detail': 'Not Found'},
                status=HTTP_404_NOT_FOUND
            )
        if course.owner != request.user:
            return DRFResponse(
                {'detail': 'Not allowed'},
                status=HTTP_403_FORBIDDEN,
            )
        serializer: CourseSerializer = CourseSerializer(
            course,
            data=request.data
        )
        if not serializer.is_valid():
            return DRFResponse(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )
        serializer.save()

        return DRFResponse(
            serializer.data,
            status=HTTP_200_OK
        )

    def destroy(
            self,
            request: DRFRequest,
            *args: tuple[Any, ...],
            **kwargs: dict[str, Any],
    ) -> DRFResponse:
        """
        Full update of the course
        """
        pk = kwargs.get('pk')

        try:
            course = self.get_queryset().get(pk=pk)
        except CourseModule.DoesNotExist:
            return DRFResponse(
                {'detail': 'Not Found'},
                status=HTTP_404_NOT_FOUND
            )
        if course.owner != request.user:
            return DRFResponse(
                {'detail': 'Not Allowed'},
                status=HTTP_403_FORBIDDEN,
            )

        course.deleted_at = timezone.now()
        course.save()
        return DRFResponse(
            status=HTTP_204_NO_CONTENT,
        )


    def activate(
            self,
            request: DRFRequest,
            *args: tuple[Any, ...],
            **kwargs: dict[str, Any],
    ) -> DRFResponse:
        pk = kwargs.get('pk')

        try:
            course = self.get_queryset().get(pk=pk)
        except CourseModule.DoesNotExist:
            return DRFResponse(
                {'detail': 'Not Found'},
                status=HTTP_404_NOT_FOUND
            )
        if course.owner != request.user:
            return DRFResponse(
                {'detail': 'Not Allowed'},
                status=HTTP_403_FORBIDDEN,
            )
        if course.is_active:
            return DRFResponse(
                {'detail': "Course is already active"},
                status=HTTP_400_BAD_REQUEST
            )
        serializer: CourseSerializer = CourseSerializer(course)
        course.is_active = True
        course.save()
        return DRFResponse(
            data=serializer.data,
            status=HTTP_200_OK,
        )

    def deactivate(
            self,
            request: DRFRequest,
            *args: tuple[Any, ...],
            **kwargs: dict[str, Any],
    ) -> DRFResponse:
        pk = kwargs.get('pk')

        try:
            course = self.get_queryset().get(pk=pk)
        except CourseModule.DoesNotExist:
            return DRFResponse(
                {'detail': 'Not Found'},
                status=HTTP_404_NOT_FOUND
            )
        if course.owner != request.user:
            return DRFResponse(
                {'detail': 'Not Allowed'},
                status=HTTP_403_FORBIDDEN,
            )
        if not course.is_active:
            return DRFResponse(
                {'detail': "Course is already inactive"},
                status=HTTP_400_BAD_REQUEST
            )
        serializer: CourseSerializer = CourseSerializer(course)
        course.is_active = False
        course.save()
        return DRFResponse(
            data=serializer.data,
            status=HTTP_200_OK,
        )


class LessonsViewSet(ViewSet):
    """
    Lesson endpoints
    """
    def get_queryset(self):
        return (LessonModule.objects
                .filter(deleted_at__isnull=True)
                .select_realated('courses'))


    def list(
            self,
            request: DRFRequest,
            *args: tuple[Any, ...],
            **kwargs: dict[str, Any],
    ) -> DRFResponse:
        course_id =kwargs.get('pk')
        try:
            course: CourseModule = CourseModule.objects.get(pk=course_id, deleted_at__isnull=True)
        except CourseModule.DoesNotExist:
            DRFResponse(
                {'detail': 'Course Not Found'},
                status=HTTP_404_NOT_FOUND
            )
        lessons = self.get_queryset().filter(course=course).orser_by('order')
        serializer: LessonSerializer = LessonSerializer(lessons, many=True)
        return DRFResponse(
            data=serializer.data,
            status=HTTP_200_OK
        )


    def create(
            self,
            request: DRFRequest,
            *args: tuple[Any, ...],
            **kwargs: dict[str, Any],
    ) -> DRFResponse:
        serializer: LessonSerializer = LessonSerializer(data=request.data)
        if not serializer.is_valid():
            return DRFResponse(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )
        course_id = request.data.get('course')
        try:
            course: CourseModule = CourseModule.objects.get(pk=course_id, deleted_at__isnull=True)
        except CourseModule.DoesNotExist:
            DRFResponse(
                {'detail': 'Course Not Found'},
                status=HTTP_404_NOT_FOUND
            )
        if course.owner != request.user:
            return DRFResponse(
                {'detail': 'Not allowed'},
                status=HTTP_403_FORBIDDEN,
            )
        min_order = (self.get_queryset()
                     .filter(course=course)
                     .aggregate(min_order=Min('order'))['min_order'])
        new_order = min_order - 1 if min_order is not None else 1

        lesson = serializer.save(course=course, order=new_order, deleted_at=None)
        return DRFResponse(
            data=serializer.data,
            status=HTTP_201_CREATED
        )


