from django.shortcuts import render
from .JSONSerializer import *
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import Context
import json


@login_required(login_url='/login/')
def game_view(request):
    return render(request, "kviz/index.html", {})


def score_update_view(request):
    user = request.user
    scores = UserScore.objects.get_or_create(user_id=user.id)
    if scores:
        wanted_score = scores[0]
        wanted_score.score = wanted_score.score + 1
        wanted_score.save()
        return HttpResponse(200)
    else:
        return HttpResponse(500)

class WordView(APIView):
    def get(self, request, pk):
        obj = Word.objects.filter(word_type=pk).order_by('?')[:1]
        word = obj.first().text
        return HttpResponse(word, content_type="text/plain")

