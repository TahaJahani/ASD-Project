import datetime

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
        response = client.get('/workspace/board')
        print(response.__dict__)

    def test_board_join(self):
        client = APIClient()
        client.login(username='client', password='secret')
        response = client.get('workspace/ board/join/')
        print(response.__dict__)

    def test_board_update(self):
        client = APIClient()
        client.login(username='client', password='secret')
        response = client.get('/workspace/board/update')
        print(response.__dict__)

    def test_board_invite(self):
        client = APIClient()
        client.login(username='client', password='secret')
        response = client.get('workspace/ board/invite/')
        print(response.__dict__)


class ListTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='client1', password='secret')
        board = Board.objects.create(title='board',
                                     color='green',
                                     owner=user)
        CardsList.objects.create(board=board, title='cards_list', order=CardsList.objects.filter(board=board).count())

    def test_list(self):
        cards_list = CardsList.objects.get(title="cards_list")
        self.assertEqual(cards_list.title, 'cards_list')

    def test_list_delete(self):
        client = APIClient()
        client.login(username='client', password='secret')
        response = client.get('/workspace/list/delete')
        print(response.__dict__)

    def test_list_get(self):
        client = APIClient()
        client.login(username='client', password='secret')
        response = client.get('/workspace/list/list')
        print(response.__dict__)

    def test_list_create(self):
        client = APIClient()
        client.login(username='client', password='secret')
        response = client.get('/workspace/list/create')
        print(response.__dict__)


class CardTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='client1', password='secret')
        board = Board.objects.create(title='board',
                                     color='green',
                                     owner=user)
        card_list = CardsList.objects.create(board=board, title='card_list',
                                             order=CardsList.objects.filter(board=board).count())
        Card.objects.create(card_list=card_list, title='card', order=Card.objects.filter(card_list=card_list).count(),
                            due_date=datetime.now() + timedelta(days=1), description='hi')

    def test_list(self):
        card = Card.objects.get(title="card")
        self.assertEqual(card.title, 'card')

    def test_card_create(self):
        client = APIClient()
        client.login(username='client', password='secret')
        response = client.get('/workspace/card/create')
        print(response.__dict__)

    def test_card_delete(self):
        client = APIClient()
        client.login(username='client', password='secret')
        response = client.get('/workspace/card/delete')
        print(response.__dict__)

    def test_card_update(self):
        client = APIClient()
        client.login(username='client', password='secret')
        response = client.get('/workspace/card/update')
        print(response.__dict__)
