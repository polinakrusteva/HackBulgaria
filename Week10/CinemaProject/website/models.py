from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rating = models.FloatField()


class Projections(models.Model):
    movie_type = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    movie_id = models.ForeignKey(Movie)


class Reservations(models.Model):
    username = models.CharField(max_length=50)
    row = models.IntegerField(max_length=5)
    col = models.IntegerField(max_length=5)
    projection_id = models.ForeignKey(Projections)
