from django.db import models
from orders.models import Order
from users.models import User

# Create your models here.
class Charge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    charge_id = models.CharField(max_length=50)
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.charge_id
