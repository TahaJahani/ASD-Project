from django.http import HttpResponse, JsonResponse
from django.utils import timezone

from workspace.models import Board


def create_board(request):
    # if not request.user.is_authenticated:
    #    return JsonResponse("Not authenticated")

    title = request.GET['title']
    color = request.GET['color']
    privacy = request.GET['privacy']
    create_time = timezone.now()
    if Board.objects.filter(title=title).exists():
        return JsonResponse({
            "Status": "Fail",
            "Message": 'A board with this title already exists',
        }, safe=False, status=400)

    board = Board(title=title, color=color, privacy=privacy)
    board.save()
    return JsonResponse({
        "Status": "Ok",
        "Message": "Board created",
        "Board": board.to_dict()
    }, safe=False, status=200)

def update_board(request):
    return HttpResponse('halle')


def delete_board(request):
    title = request.GET['title']
    board = Board.objects.filter(title=title)
    if not board.exists():
        return HttpResponse('there is no board with the title: ' + title)
    board.delete()
    return HttpResponse('board ' + title + ' deleted')


def read_board(request):
    return HttpResponse('ok this is the board')
