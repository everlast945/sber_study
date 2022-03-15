from django.urls import path

from utils.utils import LIST_CREATE_METHODS, RETRIEVE_UPDATE_DELETE_METHODS
from . import views

app_name = 'study'

urlpatterns = [
    path('interns/', views.InternViewSet.as_view(LIST_CREATE_METHODS), name='interns_list_create'),
    path('interns/<int:pk>/', views.InternViewSet.as_view(RETRIEVE_UPDATE_DELETE_METHODS), name='interns_manage'),
    path('subjects/', views.SubjectViewSet.as_view(LIST_CREATE_METHODS), name='subjects_list_create'),
    path('subjects/<int:pk>/', views.SubjectViewSet.as_view(RETRIEVE_UPDATE_DELETE_METHODS), name='subjects_manage'),
    path('directions/', views.DirectionViewSet.as_view(LIST_CREATE_METHODS), name='directions_list_create'),
    path('directions/<int:pk>/', views.DirectionViewSet.as_view(RETRIEVE_UPDATE_DELETE_METHODS), name='directions_manage'),
]