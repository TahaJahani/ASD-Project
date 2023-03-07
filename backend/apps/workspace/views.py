from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils import timezone

from apps.workspace.models import Board, Card


def read_board(request):
    board = Board.objects.get(title=request.GET['title'])
    return JsonResponse(board.to_dict())


def join_board(request):
    username = request.GET['username']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({'Message': 'User doesnt exit()'}, status=400)
    board_title = request.GET['board_title']
    try:
        board = Board.objects.get(title=board_title)
    except Board.DoesNotExist:
        return JsonResponse({'Message': 'Board doesnt exit()'}, status=400)

    board.users.add(user)
    board.save()
    return JsonResponse({'Message': 'joined to board'})


def create_card(request):
    card_title = request.GET['title']

    card = Card(title=card_title)

    card.save()
    return JsonResponse({
        "Status": "Ok",
        "Message": "Task created",
        "Task": card.to_dict()
    }, safe=False, status=200)


def update_card(request):
    description = request.GET['description']
    card = request.GET['card_title']
    if not description.equal(None):
        card.description = description
    card.save()
    return JsonResponse({'Message': 'card updated'}, status=200)


def delete_card(request):
    card_title = request.GET['title']
    card = Card.objects.filter(title=card_title)
    if not card.exists():
        return JsonResponse({'Message': 'there is no card with this title'})
    card.delete()
    card.save()
    return JsonResponse({'Message': 'card deleted'})


def read_card(request):
    card = Card.objects.get(title=request.GET['title'])
    return JsonResponse(card.to_dict())
