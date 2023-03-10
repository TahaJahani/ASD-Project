from django.contrib import admin

from apps.workspace.models import *

admin.site.register(Board)
admin.site.register(CardsList)
admin.site.register(Card)
admin.site.register(JoinRequest)