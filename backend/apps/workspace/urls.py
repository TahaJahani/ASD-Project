from django.urls import path

from .views import *

urlpatterns = [
    path('board/create', CreateBoard.as_view()),
    path('board/update', UpdateBoard.as_view()),
    path('board/delete', DeleteBoard.as_view()),
    path('board/list', GetBoards.as_view()),
    path('board/join', JoinBoard.as_view()),
    path('board/invite', InviteToBoard.as_view()),
    #
    # path('card', views.create_card),
    # path('card/update', views.update_card),
    # path('card/delete', views.delete_card),
    # path('card/read', views.read_card),

]
