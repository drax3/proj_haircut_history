import uuid
from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.contrib.auth import get_user_model

class Haircut(models.Model):
    id     = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    barber = models.CharField(max_length=200)
    shop   = models.CharField(max_length=200)
    price  = models.DecimalField(max_digits=6, decimal_places=2)
    date   = models.DateField()
    # date_of_cut = models.DateField()
    cutside1 = models.ImageField(upload_to='cuts/', blank=True)
    cutside2 = models.ImageField(upload_to='cuts/', blank=True)
    cutside3 = models.ImageField(upload_to='cuts/', blank=True)

    def __str__(self):
        return self.barber
    
    def get_absolute_url(self):
        return reverse('haircut_detail', kwargs={'pk':str(self.id)})
    
class Rating(models.Model):
    haircut = models.ForeignKey(
        Haircut,
        on_delete=models.CASCADE,
        related_name='ratings',
    )
    rating = models.IntegerField(validators=[MinValueValidator(0)])
    barber = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.rating)