from rest_framework import viewsets

from cinema.models import (
    Movie,
    CinemaHall,
    Genre,
    Actor,
    MovieSession
)
from cinema.serializers import (
    MovieSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer
)


class MovieViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        if self.action == ["list", "retrieve"]:
            return queryset.prefetch_related("genres", "actors")
        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self):
        queryset = MovieSession.objects.all()
        if self.action == ["list", "retrieve"]:
            return queryset.select_related(
                "movie",
                "cinema_hall",
            )
        return queryset


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
