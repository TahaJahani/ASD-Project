from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from apps.workspace.models import *
from django.shortcuts import get_object_or_404

from apps.workspace.serializers.CardSerializer import CardSerializer


class ListCards(ListAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = CardSerializer

    def get_queryset(self):
        list_id = self.request.GET.get('list_id')
        user = self.request.user
        cards = Card.objects.filter(list_id=list_id, list__board__users__in=[user]).all()
        return cards


class CreateCard(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        list_id = request.POST.get('list_id')
        related_list = List.objects.filter(pk=list_id, board__users__in=[request.user])
        related_list = get_object_or_404(related_list)
        card_title = request.POST.get('title')
        card_order = Card.objects.filter(list=related_list).count()
        card = Card.objects.create(
            list=related_list,
            order=card_order,
            title=card_title
        )
        return Response(CardSerializer(card).data)


class UpdateCard(APIView):
    authentication_classes = [TokenAuthentication]

    def psot(self, request):
        description = request.POST.get('description', None)
        title = request.POST.get('title', None)
        status = request.POST.get('status', None)
        card_id = request.POST.get('card_id')

        card = Card.objects.filter(pk=card_id, list__board__users__in=[request.user])
        card = get_object_or_404(card)

        for item in [description, title, status]:
            if item is not None:
                setattr(card, item, item)
        card.save()
        return Response({'Message': 'card updated'})


class DeleteCard(APIView):
    authentication_classes = [TokenAuthentication]

    def delete(self, request):
        card_id = request.POST.get('card_id')
        Card.objects.filter(pk=card_id, list__board__users__in=[request.user]).delete()
        return Response({'Message': 'card deleted'})
