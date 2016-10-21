from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

# /quiz/...
urlpatterns = [
    url(r'^$', views.game_view, name='game'),
    url(r'^score/$', views.score_update_view, name='increment-score'),
    url(r'^word/(?P<pk>\d+)/$', views.WordView.as_view(), name='word'),
]
