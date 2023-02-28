from django.urls import path

from . import views

urlpatterns = [
    path('board/create', views.create_board),
    path('board/update', views.update_board),
    path('board/delete', views.delete_board),
    path('board/read', views.read_board),
]
