from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username + " : " + str(self.score)


class Word(models.Model):
    word_type = models.IntegerField(default=0)  # 0 - muska imena, 1 - zenska, 2 - zivotinje, 3 - gradovi
    text = models.CharField(max_length=15)

    def __str__(self):
        return self.text
