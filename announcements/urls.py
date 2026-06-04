from django.urls import path
app_name = 'announcements'
from . import views

urlpatterns = [
    path('',        views.announcement_list,   name='announcement_list'),
    path('create/', views.create_announcement, name='create_announcement'),
]
