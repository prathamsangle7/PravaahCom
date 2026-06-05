from django.urls import path
from apps.dashboard import views

urlpatterns = [
    path('', views.activity_dashboard, name='activity_dashboard'),
]
