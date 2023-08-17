from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(User):
    class Meta:
        proxy = True

    def get_products(self):
        return[]
