from django.urls import path

from . import views

urlpatterns = [
    path('board/create', views.create_board),
    path('board/update', views.update_board),
    path('board/delete', views.delete_board),
    path('board/read', views.read_board),
    path('join-board', views.join_board),

    path('task/create', views.create_task),
    path('task/update', views.update_task),
    path('task/delete', views.delete_task),
    path('task/read', views.read_task),

]
