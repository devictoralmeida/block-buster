from django.db import models
from django.utils import timezone
from movies.models import Movie
from users.models import User


class MovieOrder(models.Model):
    purchased_at = models.DateTimeField(auto_now_add=timezone.now())
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
