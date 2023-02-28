from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.utils import timezone

from workspace.models import Board, Task


def create_board(request):
    # if not request.user.is_authenticated:
    #    return JsonResponse("Not authenticated")

    board_title = request.GET['title']
    board_color = request.GET['color']
    privacy = request.GET['privacy']
    create_time = timezone.now()
    if Board.objects.filter(title=board_title).exists():
        return JsonResponse({
            "Status": "Fail",
            "Message": 'A board with this title already exists',
        }, safe=False, status=400)

    board = Board(title=board_title, color=board_color, privacy=privacy)
    board.save()
    return JsonResponse({
        "Status": "Ok",
        "Message": "Board created",
        "Board": board.to_dict()
    }, safe=False, status=200)


def update_board(request):
    previous_board_title = request.GET('title')
    new_board_title = request.GET('new_title')
    board = Board.objects.filter(title=previous_board_title).first()
    board.title = new_board_title
    board.save()

    return JsonResponse({'Message': ' ok'}, status=200)


def delete_board(request):
    title = request.GET['title']
    board = Board.objects.get(title=title)
    if not board.exists():
        return HttpResponse('there is no board with the title: ' + title)
    board.delete()
    return HttpResponse('board ' + title + ' deleted')


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
    return JsonResponse


def create_task(request):
    task_title = request.GET['title']

    task = Task(title=task_title)
    return JsonResponse({'Message': 'task created'})


def update_task(request):
    return None


def delete_task(request):
    return None


def read_task(request):
    return None
