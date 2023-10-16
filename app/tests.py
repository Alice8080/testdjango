from django.test import TestCase
from .models import *

class AlbumTestCase(TestCase):
    def setUp(self):
        artist = Artist.objects.create(name="Artist1")
        artist.album_set.create(name="Album1", year=2022)
        artist.album_set.create(name="Album2", year=2023)
        album = Album.objects.get(name="Album1")
        album.track_set.create(name="Track1")
        album.track_set.create(name="Track2")
        album.track_set.create(name="Track3")

    def test_animals_can_speak(self):
        artist = Artist.objects.get(name="Artist1")
        album = Album.objects.get(name="Album1")
        track = Track.objects.get(name="Track1")
        self.assertEqual(artist.name, "Artist1")
        self.assertEqual(album.artist.name, "Artist1")
        self.assertEqual(track.album.name, "Album1")