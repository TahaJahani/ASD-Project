from django.urls import path

from .views import *

urlpatterns = [
    path('board/create', CreateBoard.as_view()),
    path('board/update', UpdateBoard.as_view()),
    path('board/delete', DeleteBoard.as_view()),
    path('board/list', GetBoards.as_view()),
    path('board/join', JoinBoard.as_view()),
    path('board/invite', InviteToBoard.as_view()),

    path('list/list', ListLists.as_view()),
    path('list/create', CreateList.as_view()),

    path('card/create', CreateCard.as_view()),
    path('card/update', UpdateCard.as_view()),
    path('card/delete', DeleteCard.as_view()),
    path('card/read', ListCards.as_view()),

]
