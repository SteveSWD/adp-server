from django.urls import path, include

from . import views
urlpatterns = [
        path('tasks/', views.tasks, name='tasks'),
        path('update/', views.update, name='result'),
        path('new/', views.new, name='new')
]
