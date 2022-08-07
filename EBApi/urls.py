"""Defines URL patterns for EBApi."""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'EBApi'
urlpatterns = [
    # Home page
    # path('', views.index, name='index'),
    path('properties/', views.PropertyList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)