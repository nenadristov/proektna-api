from rest_framework import serializers
from .models import Passengers, Flights


class PassengersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passengers
        fields = ('id', 'First_Name', 'Last_Name', 'Birth', 'Passport_Number')


class FlightsSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Flights
        fields = ('id', 'Flight_Number', 'Departure', 'Destination', 'Departure_date', 'Return_date', 'CarryOn', 'Trolley', 'CheckIn', 'PassangerId')