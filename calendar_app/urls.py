from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='calendar_home'),
    path('weekly/', views.weekly_view, name='weekly_view'),
    path('monthly/', views.monthly_view, name='monthly_view'),
    path('unavailability/', views.unavailability_view, name='unavailability_view'),
]
