from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import *
from .models import *

# Обработка запросов к API
class DataView(APIView):
    def get(self, request):
        # Формирование списка словарей с данными
        def form_list_items(album):
            tracks = Track.objects.filter(album=album)
            tracks_names = [track.name for track in tracks]
            item = {
                "album": album.__str__(),
                "name": album.name,
                "artist@name": album.artist.name,
                "tracks": tracks_names
            }
            return item
        albums = Album.objects.all()
        response = list(map(lambda album: form_list_items(album), albums))

        # Обработка сортировки по параметру, если он передан
        sorting = self.request.GET.get('sorting')
        if sorting:
            params = sorting.split("@")

            # Обработка ошибки, если в sorting передается параметр, не содержащийся в колонках ответа
            default_sort_param = "album" # В этом случае сортировка происходит по умолчанию (по текстовому представлению)
            if len(response) > 0 and params[0] not in response[0]: 
                sorting = default_sort_param
            
            def sort_response(item):
                if len(params) > 100:
                    # Логика, по которой вложенные поля разделяются знаком ’@’
                    # и сортировка происходит по вложенным полям
                    result = item[params[0]]
                    for i in range(len(params)):
                        if params[i] in result: 
                            result = result[params[i]]
                        else:
                            return result
                    return result
                else:
                    # Логика для сортировки по текстовому представлению
                    return item[sorting]
            response.sort(key=sort_response)
        return Response(response)

# Представление форм на главной странице
def index(request):
    artist_form = ArtistForm()
    album_form = AlbumForm()
    track_form = TrackForm()
    data = {
            "artist_form": artist_form, 
            "album_form": album_form, 
            "track_form": track_form
        }

    if request.method == "POST":
        form_type = request.POST.get("type")
        if form_type == "artist":
            form = ArtistForm(request.POST)
        elif form_type == "album":
            form = AlbumForm(request.POST)
        elif form_type == "track":
            form = TrackForm(request.POST)
        
        if form.is_valid():
            form.save()
            data["response"] = "Data saved"
        else:
            data["response"] = "An error occurred while saving data"
            
    return render(request, "index.html", context=data)
