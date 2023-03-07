from django.urls import path

from .views import *

urlpatterns = [
    path('board/create', CreateBoard.as_view()),
    path('board/update', UpdateBoard.as_view()),
    path('board/delete', views.delete_board),
    path('board/read', views.read_board),
    path('join-board', views.join_board),

    path('card', views.create_card),
    path('card/update', views.update_card),
    path('card/delete', views.delete_card),
    path('card/read', views.read_card),

]
