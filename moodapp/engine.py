# engine.py

import random
from moodapp.database import TRACKS_DB, QUESTIONS

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings


def get_spotify_client():
    """
    Създава и връща Spotify клиент, аутентикиран чрез Client Credentials Flow
    (без потребителски логин - само за достъп до публичния каталог).
    """
    auth_manager = SpotifyClientCredentials(
        client_id=settings.SPOTIPY_CLIENT_ID,
        client_secret=settings.SPOTIPY_CLIENT_SECRET
    )
    return spotipy.Spotify(auth_manager=auth_manager)

# Свързваме нашите mood-ове с жанрове/думи за търсене в Spotify
MOOD_TO_SEARCH_TERM = {
    "happy": "happy pop upbeat",
    "sad": "sad emotional ballad",
    "chill": "chill relax lofi",
    "angry": "angry rock metal energetic",
}


def fetch_tracks_from_spotify(mood, limit=8, include_surprise=False):
    """
    Търси песни в Spotify по зададено настроение и връща списък от
    речници в същия формат като TRACKS_DB. Ако include_surprise е True,
    добавя 1 допълнителна песен от различно настроение.
    """
    sp = get_spotify_client()
    search_term = MOOD_TO_SEARCH_TERM.get(mood, mood)

    results = sp.search(q=search_term, type="track", limit=limit)

    tracks = []
    for item in results["tracks"]["items"]:
        tracks.append({
            "title": item["name"],
            "artist": item["artists"][0]["name"],
            "genre": search_term,
            "mood": mood,
        })

    if include_surprise:
        other_moods = [m for m in MOOD_TO_SEARCH_TERM if m != mood]
        surprise_mood = random.choice(other_moods)
        surprise_term = MOOD_TO_SEARCH_TERM[surprise_mood]

        surprise_results = sp.search(q=surprise_term, type="track", limit=1)
        if surprise_results["tracks"]["items"]:
            item = surprise_results["tracks"]["items"][0]
            tracks.append({
                "title": item["name"],
                "artist": item["artists"][0]["name"],
                "genre": surprise_term,
                "mood": surprise_mood,
            })

    return tracks


def calculate_mood(user_answers):
    """
    Приема списък от избраните опции (напр. ['A', 'C', 'B', 'A'])
    и изчислява кое настроение има най-много точки.
    """
    # Инициализираме брояча на точки за всяко настроение
    scores = {"happy": 0, "sad": 0, "chill": 0, "angry": 0}
    
    # Обхождаме въпросите и отговорите едновременно
    for question, answer in zip(QUESTIONS, user_answers):
        # Проверяваме дали отговорът е валиден за дадения въпрос
        if answer in question["options"]:
            option_data = question["options"][answer]
            mood = option_data["mood_impact"]
            points = option_data["points"]
            scores[mood] += points
            
    # Намираме настроението с максимален брой точки
    # Ако има равенство, max() взема първото срещнато
    detected_mood = max(scores, key=scores.get)
    return detected_mood


def generate_playlist(mood, include_surprise=False):
    """
    Генерира плейлист на базата на определеното настроение.
    Ако include_surprise е True, добавя една произволна песен от друго настроение.
    """
    # 1. Филтрираме песните, които отговарят точно на нашето настроение
    matching_tracks = [track for track in TRACKS_DB if track["mood"] == mood]
    
    # Правим копие на филтрираните песни, за да не променяме оригиналната база
    playlist = matching_tracks.copy()
    
    # 2. Логика за "Изненада плейлист"
    if include_surprise:
        # Взимаме всички песни, които НЕ съвпадат с текущото настроение
        surprise_pool = [track for track in TRACKS_DB if track["mood"] != mood]
        
        if surprise_pool:
            # Избираме една случайна песен за изненада
            surprise_track = random.choice(surprise_pool)
            playlist.append(surprise_track)
            
    return playlist


def get_mood_tip(mood):
    """
    Връща текстова препоръка/съвет според настроението.
    """
    tips = {
        "happy": "Страхотно е, че си в такова настроение! Усмихнете се на първата песен и споделете енергията с някого!",
        "sad": "Нормално е да има и такива дни. Сипете си нещо топло, завийте се и се отпуснете с музиката.",
        "chill": "Перфектно време за релакс. Опитайте да затворите очи и просто да слушате без да мислите за задачи.",
        "angry": "Изкарайте напрежението! Пуснете си музиката силно, тренирайте или просто подишайте дълбоко."
    }
    return tips.get(mood, "Насладете се на музиката!")

def format_playlist_for_export(mood, playlist, tip):
    """
    Превръща плейлиста в четим текст, готов за запис/сваляне като .txt файл.
    """
    lines = []
    lines.append("=" * 40)
    lines.append("MOODIFY — Твоят плейлист")
    lines.append("=" * 40)
    lines.append(f"Настроение: {mood.upper()}")
    lines.append("")
    lines.append("Песни:")
    
    for idx, track in enumerate(playlist, 1):
        lines.append(f"{idx}. {track['title']} — {track['artist']} ({track['genre']})")
    
    lines.append("")
    lines.append(f"Съвет: {tip}")
    lines.append("=" * 40)
    
    return "\n".join(lines)