from django.contrib import admin
from django.db.models import Avg
from .models import Haircut, Rating

class RatingInline(admin.TabularInline):
    model = Rating

class HaicutAdmin(admin.ModelAdmin):
    inlines = [
        RatingInline,
    ]
    def avg_rating(self, obj):
        return obj.ratings.aggregate(avg_rating=Avg('rating'))['avg_rating']
    avg_rating.short_description = 'Average Rating'

    list_display = ("barber", "shop", "price", "date", "avg_rating")


admin.site.register(Haircut, HaicutAdmin)