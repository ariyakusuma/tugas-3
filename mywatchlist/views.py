from django.shortcuts import render
from mywatchlist.models import MovieList
from django.http import HttpResponse
from django.core import serializers


def show_watchlist(request):
    data_movie_watchlist = MovieList.objects.all()
    context = {
        'list_movie': data_movie_watchlist,
        'nama': 'Ariya',
        'npm': '2106751991'
}
    return render(request, "mywatchlist.html", context)

# Create your views here.
def show_xml(request):
    data = MovieList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = MovieList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_html(request):
    data = MovieList.objects.all()
    return HttpResponse(serializers.serialize("html", data), content_type="application/html")

def show_json_by_id(request, id):
    data = MovieList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MovieList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


