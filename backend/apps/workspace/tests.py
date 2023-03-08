from django.test import TestCase
from django.urls import reverse

from .models import *


class BoardTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='Ali')
        Board.objects.create(title='board',
                             background='green',
                             visibility='public',
                             owner=user)

    def test_board(self):
        board = Board.objects.get(title="board")
        self.assertEqual(board.title, 'board')

    def test_view1(self):
        response = self.client.get(reverse('create-board'),
                                   {'title': 'title1', 'visibility': 'v1', 'background': 'red'}
                                   )
        print(response)
        self.assertEqual(response.status_code, 200)
