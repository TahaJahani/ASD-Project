from django.test import TestCase
from rest_framework.test import APIClient

from .models import *


class BoardTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='client', password='secret')
        Board.objects.create(title='board',
                             color='green',
                             owner=user)

    def test_board(self):
        board = Board.objects.get(title="board")
        self.assertEqual(board.title, 'board')

    def test_board_get(self):
        client = APIClient()
        client.login(username='client', password='secret')
        response = client.get('/workspace/board/list')
        print(response.__dict__)


class ListTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='client', password='secret')
        Board.objects.create(title='board',
                             color='green',
                             owner=user)

    def test_list(self):
        board = Board.objects.get(title="board")
        self.assertEqual(board.title, 'board')

    def test_list_get(self):
        client = APIClient()
        client.login(username='client', password='secret')
        response = client.get('/workspace/board/list')
        print(response.__dict__)
