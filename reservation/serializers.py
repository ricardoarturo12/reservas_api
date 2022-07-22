from rest_framework import serializers
from .models import Person, Client, Room, Reservation

# create a serializer ()
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')


# create a serializer ()
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')


# create a serializer ()
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('__all__')



class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ('__all__')


