from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    OrderViewSet,
    TicketViewSet,
    MovieSessionViewSet
)

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_session"
)
router.register(
    "cinema_halls",
    CinemaHallViewSet,
    basename="cinema-hall"
)
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")
router.register("orders", OrderViewSet, basename="order")
router.register("tickets", TicketViewSet, basename="ticket")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
