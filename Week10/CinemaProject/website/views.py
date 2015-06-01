from django.shortcuts import render
from .models import Movie, Projections, Reservations


def index(request):
    return render(request, "index.html", locals())
