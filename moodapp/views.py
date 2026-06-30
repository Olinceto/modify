from django.shortcuts import render
from django.http import HttpResponse
from .database import QUESTIONS
from .engine import (
    calculate_mood,
    get_mood_tip,
    format_playlist_for_export,
    fetch_tracks_from_spotify,
)


def quiz_view(request):
    """
    Показва въпросника на потребителя (GET заявка).
    """
    context = {
        "questions": QUESTIONS
    }
    return render(request, "moodapp/quiz.html", context)


def result_view(request):
    """
    Обработва изпратената форма (POST) и показва резултата.
    """
    if request.method != "POST":
        return render(request, "moodapp/quiz.html", {"questions": QUESTIONS})

    user_answers = []
    for i in range(1, len(QUESTIONS) + 1):
        answer = request.POST.get(f"question_{i}")
        user_answers.append(answer)

    include_surprise = "include_surprise" in request.POST

    mood = calculate_mood(user_answers)
    playlist = fetch_tracks_from_spotify(mood, limit=8, include_surprise=include_surprise)
    tip = get_mood_tip(mood)

    context = {
        "mood": mood,
        "playlist": playlist,
        "tip": tip,
        "has_surprise": include_surprise,
    }
    return render(request, "moodapp/result.html", context)


def download_playlist_view(request):
    """
    Регенерира плейлиста от данните в URL-а и го връща като файл за сваляне.
    """
    mood = request.GET.get("mood")
    include_surprise = request.GET.get("surprise") == "1"

    playlist = fetch_tracks_from_spotify(mood, limit=8, include_surprise=include_surprise)
    tip = get_mood_tip(mood)

    export_text = format_playlist_for_export(mood, playlist, tip)

    response = HttpResponse(export_text, content_type="text/plain")
    response["Content-Disposition"] = f'attachment; filename="moodify_{mood}_playlist.txt"'
    return response