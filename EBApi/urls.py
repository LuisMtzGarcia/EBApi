"""Defines URL patterns for EBApi."""

from django.urls import path

from . import views

app_name = 'EBApi'
urlpatterns = [
    # Home page
    path('', views.properties, name='index'),
    # Property List 
    path('properties/<int:page>', views.properties, name="properties"),
    path('properties/', views.properties, name="properties"),
    # Property Detail
    path('property/<str:id>', views.property_detail, name="property"),
    # Contact request form
    path('contact_request/<str:id>', views.contact_request, name="contact_requests"),
]
