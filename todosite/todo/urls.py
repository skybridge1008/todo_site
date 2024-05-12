from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:pk>/', views.todo_detail, name='todo_detail'),
    path('post/', views.todo_post, name='todo_post'),
    path('<int:pk>/edit/', views.todo_edit, name='todo_edit'),
    path('done/', views.todo_done_list, name='todo_done_list'),
    path('done/<int:pk>', views.todo_done, name='todo_done'),
    path('done/<int:pk>/delete/', views.todo_delete, name='todo_delete'),
    path('done/<int:pk>/rollback/', views.todo_rollback, name='todo_rollback'),
]