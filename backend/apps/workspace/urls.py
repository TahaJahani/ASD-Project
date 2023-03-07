from django.urls import path

from .views import *

urlpatterns = [
    path('board/create', CreateBoard.as_view()),
    path('board/update/<pk>', UpdateBoard.as_view()),
    path('board/delete/<pk>', DeleteBoard.as_view()),
    path('board/list', GetBoards.as_view()),
    path('board/join/<token>', JoinBoard.as_view()),
    path('board/invite/<pk>', InviteToBoard.as_view()),

    path('list/list', ListLists.as_view()),
    path('list/create', CreateList.as_view()),
    path('list/update', UpdateList.as_view()),
    path('list/delete/<pk>', DeleteList.as_view()),

    path('card/create', CreateCard.as_view()),
    path('card/update', UpdateCard.as_view()),
    path('card/delete', DeleteCard.as_view()),
    path('card/read', ListCards.as_view()),

]
