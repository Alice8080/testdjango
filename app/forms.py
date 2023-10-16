from .models import *
from django.forms import ModelForm

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

class TrackForm(ModelForm):
    class Meta:
        model = Track
        fields = '__all__'
