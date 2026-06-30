from django.urls import path
from . import views

urlpatterns = [
    path("", views.quiz_view, name="quiz"),
    path("result/", views.result_view, name="result"),
    path("download/", views.download_playlist_view, name="download"),
]