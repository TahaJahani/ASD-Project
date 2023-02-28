from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    privacy = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, null=True)

    def to_dict(self):
        return {
            "title": self.title,
            "color": self.color,
            "privacy": self.privacy
        }


class Task(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
