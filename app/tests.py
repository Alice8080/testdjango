from django.test import TestCase
from rest_framework.test import APIClient
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

    def test_post_data(self):
        artist = Artist.objects.get(name="Artist1")
        album = Album.objects.get(name="Album1")
        track = Track.objects.get(name="Track1")
        self.assertEqual(artist.name, "Artist1")
        self.assertEqual(album.artist.name, "Artist1")
        self.assertEqual(track.album.name, "Album1")

    def test_api_requests(self):
        client = APIClient()
        request = client.get('/api/data', format='json')
        request_sorting = client.get('/api/data?sorting=name', format='json')
        data = [{'album': 'Album1[2022]', 'name': 'Album1', 'artist@name': 'Artist1', 'tracks': ['Track1', 'Track2', 'Track3']}, {'album': 'Album2[2023]', 'name': 'Album2', 'artist@name': 'Artist1', 'tracks': []}]
        self.assertEqual(request.data, data)
        self.assertEqual(request_sorting.data, data)