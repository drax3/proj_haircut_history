from rest_framework import serializers
from haircuts.models import Haircut

class HaircutSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'barber', 'shop')
        model = Haircut