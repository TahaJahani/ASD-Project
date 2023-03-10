import uuid

from django.contrib.auth.models import User
from django.db import models


class ResetPassword(models.Model):
    token = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_used = models.BooleanField(default=False)

    @staticmethod
    def get_unique_token():
        for i in range(10):
            token = uuid.uuid1()
            if not ResetPassword.objects.filter(token=token).exists():
                return token
        else:
            raise Exception("Cannot Save Model!")
