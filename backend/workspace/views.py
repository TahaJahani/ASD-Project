from django.contrib.auth.models import User
from django.http import JsonResponse

from workspace.models import Board, Card


def create_board(request):
    # if not request.user.is_authenticated:
    #    return JsonResponse("Not authenticated")

    board_title = request.GET['title']
    board_bg = request.GET['background']
    visibility = request.GET['visibility']
    if Board.objects.filter(title=board_title).exists():
        return JsonResponse({
            "Status": "Fail",
            "Message": 'A board with this title already exists',
        }, safe=False, status=400)

    board = Board(title=board_title, background=board_bg, visibility=visibility)
    board.save()
    return JsonResponse({
        "Status": "Ok",
        "Message": "Board created",
        "Board": board.to_dict()
    }, safe=False, status=200)


def update_board(request):
    previous_board_title = request.GET('title')
    new_board_title = request.GET('new_title')
    new_board_background = request.GET('new_background')
    board = Board.objects.filter(title=previous_board_title).first()
    board.title = new_board_title
    if not new_board_background.equal(None):
        board.background = new_board_background
    board.save()

    return JsonResponse({'Message': ' ok'}, status=200)


def delete_board(request):
    title = request.GET['title']
    board = Board.objects.filter(title=title)
    if not board.exists():
        return JsonResponse({'Message': 'there is no board with this title'})
    board.delete()
    board.save()
    return JsonResponse({'Message': 'board deleted'})


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
    card_title = request.GET['card_title']
    card = Card.objects.filter(title=card_title)
    description = request.GET['description']
    due_date = request.GET['due_date']

    if not description.equal(None):
        card.description = description
    if not due_date.equal(None):
        card.due_date = due_date

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
