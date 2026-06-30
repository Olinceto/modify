from django.test import TestCase
from .engine import calculate_mood, generate_playlist, format_playlist_for_export


class TestCalculateMood(TestCase):

    def test_all_happy_answers(self):
        answers = ["A", "A", "A", "A"]
        result = calculate_mood(answers)
        self.assertEqual(result, "happy")

    def test_all_sad_answers(self):
        answers = ["B", "B", "B", "B"]
        result = calculate_mood(answers)
        self.assertEqual(result, "sad")

    def test_all_chill_answers(self):
        answers = ["C", "C", "C", "C"]
        result = calculate_mood(answers)
        self.assertEqual(result, "chill")

    def test_all_angry_answers(self):
        answers = ["D", "D", "D", "D"]
        result = calculate_mood(answers)
        self.assertEqual(result, "angry")

    def test_mixed_answers_picks_majority(self):
        answers = ["A", "A", "A", "B"]
        result = calculate_mood(answers)
        self.assertEqual(result, "happy")


class TestGeneratePlaylist(TestCase):

    def test_playlist_contains_only_matching_mood_without_surprise(self):
        playlist = generate_playlist("happy", include_surprise=False)
        for track in playlist:
            self.assertEqual(track["mood"], "happy")

    def test_playlist_with_surprise_has_one_extra_track(self):
        playlist_without = generate_playlist("happy", include_surprise=False)
        playlist_with = generate_playlist("happy", include_surprise=True)
        self.assertEqual(len(playlist_with), len(playlist_without) + 1)


class TestFormatPlaylistForExport(TestCase):

    def test_export_contains_mood_and_tip(self):
        sample_playlist = [
            {"title": "Test Song", "artist": "Test Artist", "genre": "Pop", "mood": "happy"}
        ]
        result = format_playlist_for_export("happy", sample_playlist, "Усмихни се!")
        self.assertIn("HAPPY", result)
        self.assertIn("Test Song", result)
        self.assertIn("Test Artist", result)
        self.assertIn("Усмихни се!", result)

    def test_export_returns_string(self):
        result = format_playlist_for_export("sad", [], "някакъв съвет")
        self.assertIsInstance(result, str)