from django.db import models
from .customer import Customer
from .product import Product


class Recommendation(models.Model):

    customer = models.ForeignKey(Customer, related_name='recommendations_receiver', on_delete=models.DO_NOTHING,)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING,)
    recommender = models.ForeignKey(Customer, related_name='recommendations_giver', on_delete=models.DO_NOTHING,)
