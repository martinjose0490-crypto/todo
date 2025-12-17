from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.todo_upsert, name='todo_add'),
    path('edit/<int:pk>/', views.todo_upsert, name='todo_edit'),
    path('view/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
]
