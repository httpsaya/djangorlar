from django.urls import path
from .views import render_count

urlpatterns=[
    path('', render_count)
]