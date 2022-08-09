"""Defines URL patterns for EBApi."""

from django.urls import path

from . import views

app_name = 'EBApi'
urlpatterns = [
    # Home page
    # path('', views.index, name='index'),
    path('properties/<int:page>', views.properties, name="properties"),
    path('properties/', views.properties, name="properties"),
]
