from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils import timezone

from apps.workspace.models import Board, Card



def read_card(request):
    card = Card.objects.get(title=request.GET['title'])
    return JsonResponse(card.to_dict())
