from django.urls import path
from . import views

urlpatterns = [
    path('', views.bug_list, name='bug_list'),
    path('bug/<int:pk>/', views.bug_detail, name='bug_detail'),
    path('bug/new/', views.bug_create, name='bug_create'),
    path('bug/<int:pk>/edit/', views.bug_update, name='bug_update'),
]
