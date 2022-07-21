from dataclasses import fields
from rest_framework import serializers
from .models import Person, Client, Room, Reservation
from django.http import Http404
from rest_framework.response import Response

# create a serializer ()
class PersonSerializer(serializers.ModelSerializer):
    # initialize model and fields you want to serialize
    class Meta:
        model = Person
        fields = ('__all__')


# create a serializer ()
class ClientSerializer(serializers.ModelSerializer):
    # initialize model and fields you want to serialize
    class Meta:
        model = Client
        fields = ('__all__')


# create a serializer ()
class RoomSerializer(serializers.ModelSerializer):
    # initialize model and fields you want to serialize
    class Meta:
        model = Room
        fields = ('__all__')



class ReservationSerializer(serializers.ModelSerializer):
    # persons = serializers.SlugRelatedField(
    #     many=True,
    #     queryset=Person.objects.all(),
    #     slug_field='identification'
    # ) 
    # initialize model and fields you want to serialize
    class Meta:
        model = Reservation
        fields = ('__all__')

    # def to_representation(self, instance):
    #     self.fields['persons'] =  PersonSerializer(read_only=True, many=True)
    #     self.fields['client_id'] =  ClientSerializer(read_only=True)
    #     self.fields['romm_id'] =  RoomSerializer(read_only=True)
    #     return super(ReservationSerializer, self).to_representation(instance)

