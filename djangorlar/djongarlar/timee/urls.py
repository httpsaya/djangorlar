from django.urls import path
from .views import render_time

urlpatterns=[
    path('', render_time),
]
