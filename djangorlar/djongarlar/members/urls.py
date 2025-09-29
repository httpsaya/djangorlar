from django.urls import path
from .views import render_users, context, render_user
urlpatterns=[
    path('', render_users),
    path('<int:id>user/', render_user),
]