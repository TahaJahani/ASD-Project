from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils import timezone

from apps.workspace.models import Board, Card


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
