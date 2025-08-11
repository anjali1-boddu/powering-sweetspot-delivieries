from django.db import models
from django.db import models
from authentication.models import User
from cakes.models import Cake

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # e.g. 1 to 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'cake')  # one review per user per cake

    def __str__(self):
        return f'{self.user.username} - {self.cake.name} ({self.rating})'
