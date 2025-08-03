from django.db import models
from authentication.models import User
from cakes.models import Cake

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    message = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.cake.name} x {self.quantity}"
