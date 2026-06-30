# database.py

# 1. Локална база данни с песни, разделени по настроения (Moods)
TRACKS_DB = [
    # HAPPY MOOD
    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": "Pop", "mood": "happy"},
    {"title": "Walking On Sunshine", "artist": "Katrina and the Waves", "genre": "Rock", "mood": "happy"},
    {"title": "Can't Stop the Feeling!", "artist": "Justin Timberlake", "genre": "Pop", "mood": "happy"},
    
    # SAD MOOD
    {"title": "Someone Like You", "artist": "Adele", "genre": "Pop", "mood": "sad"},
    {"title": "Fix You", "artist": "Coldplay", "genre": "Alternative", "mood": "sad"},
    {"title": "All I Want", "artist": "Kodaline", "genre": "Indie", "mood": "sad"},
    
    # CHILL MOOD
    {"title": "Sunflower", "artist": "Post Malone", "genre": "Hip-Hop", "mood": "chill"},
    {"title": "Weightless", "artist": "Marconi Union", "genre": "Ambient", "mood": "chill"},
    {"title": "Come Fly With Me", "artist": "Frank Sinatra", "genre": "Jazz", "mood": "chill"},
    
    # ANGRY MOOD
    {"title": "In The End", "artist": "Linkin Park", "genre": "Rock", "mood": "angry"},
    {"title": "Bulls on Parade", "artist": "Rage Against The Machine", "genre": "Metal", "mood": "angry"},
    {"title": "The Trooper", "artist": "Iron Maiden", "genre": "Metal", "mood": "angry"},
]

# 2. Въпросник за определяне на настроението
QUESTIONS = [
    {
        "text": "Каква е перфектната атмосфера за теб в момента?",
        "options": {
            "A": {"text": "Пълно парти, силна музика и хора", "mood_impact": "happy", "points": 2},
            "B": {"text": "Тиха стая, приглушена светлина и самота", "mood_impact": "sad", "points": 2},
            "C": {"text": "Природа, чист въздух и пълна тишина", "mood_impact": "chill", "points": 2},
            "D": {"text": "Тежък трафик, лудница, всичко ме дразни", "mood_impact": "angry", "points": 2}
        }
    },
    {
        "text": "Ако сега си поръчаш напитка, каква ще е тя?",
        "options": {
            "A": {"text": "Коктейл или нещо цветно и сладко", "mood_impact": "happy", "points": 2},
            "B": {"text": "Просто вода... нямам сили за нищо", "mood_impact": "sad", "points": 2},
            "C": {"text": "Топъл чай или горещ шоколад", "mood_impact": "chill", "points": 2},
            "D": {"text": "Двойно еспресо или енергийна напитка", "mood_impact": "angry", "points": 2}
        }
    },
    {
        "text": "Представи си, че имаш неочаквано свободен следобед. Какво ще направиш?",
        "options": {
            "A": {"text": "Ще звънна на приятели да излезем веднага", "mood_impact": "happy", "points": 2},
            "B": {"text": "Ще си легна да спя или ще гледам тъжен филм", "mood_impact": "sad", "points": 2},
            "C": {"text": "Ще чета книга или ще се разходя безцелно", "mood_impact": "chill", "points": 2},
            "D": {"text": "Ще отида да тренирам здраво, за да изкарам напрежението", "mood_impact": "angry", "points": 2}
        }
    },
    {
        "text": "Кой цвят описва усещането ти в този момент?",
        "options": {
            "A": {"text": "Ярко жълто или оранжево", "mood_impact": "happy", "points": 2},
            "B": {"text": "Тъмно сиво или синьо", "mood_impact": "sad", "points": 2},
            "C": {"text": "Пастелно зелено или бежово", "mood_impact": "chill", "points": 2},
            "D": {"text": "Кърваво червено", "mood_impact": "angry", "points": 2}
        }
    }
]