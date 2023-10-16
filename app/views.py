from django.shortcuts import render
from .forms import *
from .models import *

def index(request):
    artistForm = ArtistForm()
    albumForm = AlbumForm()
    trackForm = TrackForm()
    data = {
            "artistForm": artistForm, 
            "albumForm": albumForm, 
            "trackForm": trackForm
        }
    if request.method == "POST":
        formType = request.POST.get("type")
        if formType == "artist":
            form = ArtistForm(request.POST)
        elif formType == "album":
            form = AlbumForm(request.POST)
        elif formType == "track":
            form = TrackForm(request.POST)
        if form.is_valid():
            form.save()
            data["response"] = "Data saved"
        else:
            data["response"] = "An error occurred while saving data"

    return render(request, "index.html", context=data)