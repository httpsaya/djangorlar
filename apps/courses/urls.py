# Django modules
from django.urls import path, include

# Project modules
from .views import CourseViewSet, LessonsViewSet

# Django Rest Framework modules
from rest_framework.routers import DefaultRouter


router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)
router.register(
    prefix='v1/education/courses',
    viewset= CourseViewSet,
    basename='courses',
)

router.register(
    prefix='v1/education/lessons',
    viewset= LessonsViewSet,
    basename='lessons',
)
urlpatterns = [
    # activate and deactivate
    path('v1/education/courses/<int:pk>/activate/', CourseViewSet.as_view({'post': 'activate'})),
    path('v1/education/courses/<int:pk>/deactivate/', CourseViewSet.as_view({'post': 'deactivate'})),

    path('v1/education/lessons/<int:pk>/move/', LessonsViewSet.as_view({'put': 'move'})),
    path('v1/education/courses/<int:pk>/lessons/', LessonsViewSet.as_view({'get': 'list'}), name='course-lessons'),
]
urlpatterns += router.urls
