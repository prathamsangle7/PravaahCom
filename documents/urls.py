from django.urls import path
from . import views

urlpatterns = [
    path('',                        views.document_list,      name='document_list'),
    path('upload/',                 views.upload_document,    name='upload_document'),
    path('download/<int:doc_id>/', views.download_document,  name='download_document'),
]
