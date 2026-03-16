from django.contrib import admin
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token
from django.urls import path
from . import views
from .views import TestView

urlpatterns = [
    path('test', TestView.as_view()),
]
