
from django.db import models
from django.db.models.functions import Lower

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tags = models.JSONField(default=list, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("name"), name="uniq_product_name_ci"
            )
        ]

    def __str__(self):
        return f"{self.name} (${self.price})"
