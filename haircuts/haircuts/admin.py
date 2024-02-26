from django.contrib import admin
from .models import Haircut

class HaicutAdmin(admin.ModelAdmin):
    list_display = ("barber", "shop", "price", "date")


admin.site.register(Haircut, HaicutAdmin)