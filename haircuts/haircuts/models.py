import uuid
from django.db import models
from django.urls import reverse


class Haircut(models.Model):
    id     = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    barber = models.CharField(max_length=200)
    shop   = models.CharField(max_length=200)
    price  = models.DecimalField(max_digits=6, decimal_places=2)
    date   = models.DateTimeField()

    def __str__(self):
        return self.barber
    
    def get_absolute_url(self):
        return reverse('haircut_detail', args=[str(self.id)])