from django.db import models


class RatingMovie(models.TextChoices):
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"
    G = "G"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(
        max_length=10,
        blank=True,
        default="",
    )
    rating = models.CharField(
        max_length=20,
        choices=RatingMovie.choices,
        default=RatingMovie.G,
    )

    synopsis = models.TextField(
        blank=True,
        default="",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.RESTRICT,
        related_name="movies",
    )

    ordered_by = models.ManyToManyField(
        "users.User",
        through="movies_orders.MovieOrder",
        related_name="ordered_movies",
    )
