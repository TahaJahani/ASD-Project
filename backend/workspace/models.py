from datetime import timedelta, datetime

from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    title = models.CharField(unique=True, max_length=100)
    background = models.CharField(max_length=50)
    visibility = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, null=True)

    def to_dict(self):
        return {
            "title": self.title,
            "background": self.background,
            "visibility": self.visibility
        }


class List(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    position = models.IntegerField(max_length=100)

    def to_dict(self):
        return {
            "title": self.title,
        }


class Card(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000, default=None)
    due_date = models.DateTimeField(default=datetime.now() + timedelta(days=1))

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
        }


class BoardFollowing(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
