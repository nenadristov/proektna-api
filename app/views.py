from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser 
from .models import Passengers, Flights
from .serializers import PassengersSerializer, FlightsSerializer

# Create your views here.

def home(request):
    return None

#Create Passenger
#Create Flight
@api_view(["GET", 'POST'])
def Create_passenger_flight(request):
    if request.method =='POST':
        data_patnik = {
            'First_Name': request.data.get("First_Name"),
            'Last_Name': request.data.get("Last_Name"),
            "Birth": request.data.get("Birth"),
            'Passport_Number': request.data.get("Passport_Number")
        }

        data_let = {
            "Flight_Number": request.data.get("Flight_Number"),
            "Departure": request.data.get("Departure"),
            "Destination": request.data.get("Destination"),
            "Departure_date": request.data.get("Departure_date"),
            "Return_date": request.data.get("Return_date"),
            "CarryOn":request.data.get("CarryOn"),
            "Trolley": request.data.get("Trolley"),
            "CheckIn": request.data.get("CheckIn"),
            "PassangerId": request.data.get("PassangerId")
        }

        patnik = PassengersSerializer(data = data_patnik)
        let = FlightsSerializer(data = data_let)

        if patnik.is_valid and let.is_valid:
            patnik.is_valid(raise_exception=True)
            let.is_valid(raise_exception=True)
            let.save()
            patnik.save()
           
            return Response( status=status.HTTP_201_CREATED)
        return Response(patnik.data,  status=status.HTTP_400_BAD_REQUEST)


#Get  all Passengers
@api_view(['GET'])
def get_all_passengers(request):
    if request.method == 'GET':
        posts = Passengers.objects.all()
        serializer = PassengersSerializer(posts, many=True)
        return Response(serializer.data)

#Get all Flights
@api_view(['GET'])
def get_all_flights(request):
    if request.method == 'GET':
        posts = Flights.objects.all()
        serializer = FlightsSerializer(posts, many=True)
        return Response(serializer.data)


#Get Passenger by Id
#Update Passenger
#Delete Passenger
@api_view(['GET', 'PUT', 'DELETE'])
def get_passenger_by_id(request, pk):
    try:
        passenger = Passengers.objects.get(pk = pk)
    except Passengers.DoesNotExist:
        return Response({"message": "The flight does not exist"})
    if request.method == 'GET':
        serializer = PassengersSerializer(passenger, many=True)
        return Response(serializer.data)
    
    if request.method =="DELETE":
        passenger.delete()
        return Response({"message": "The flight was succesfully deleted"})
    
    elif request.method =='PUT':
        data_patnik = {
            'First_Name': request.data.get("First_Name"),
            'Last_Name': request.data.get("Last_Name"),
            "Birth": request.data.get("Birth"),
            'Passport_Number': request.data.get("Passport_Number")
        }
        patnik = PassengersSerializer(passenger, data = data_patnik)
        #passenger_serializer = PassengersSerializer(passenger, data= passenger_data)
        if patnik.is_valid():
            patnik.save()
            return Response(patnik.data)

        return Response(passenger_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        



#Get Flights by Id
#Update Flight
#Delete Flight
@api_view(['GET', 'PUT', 'DELETE'])
def get_flights_by_id(request, pk):
    try:
        flight = Flights.objects.get(pk = pk)
    except Flights.DoesNotExist:
        return Response({"message": "The flight does not exist"})
    if request.method == 'GET':
        serializer = FlightsSerializer(flight, many=True)
        return Response(serializer.data)
    
    if request.method =="DELETE":
        flight.delete()
        return Response({"message": "The flight was succesfully deleted"})
    
    elif request.method =='PUT':
        data_let = {
            "Flight_Number": request.data.get("Flight_Number"),
            "Departure": request.data.get("Departure"),
            "Destination": request.data.get("Destination"),
            "Departure_date": request.data.get("Departure_date"),
            "Return_date": request.data.get("Return_date"),
            "CarryOn":request.data.get("CarryOn"),
            "Trolley": request.data.get("Trolley"),
            "CheckIn": request.data.get("CheckIn"),
            "PassangerId": request.data.get("PassangerId")
        }
        
        let = FlightsSerializer(flight, data = data_let)
        #passenger_serializer = PassengersSerializer(passenger, data= passenger_data)
        if let.is_valid():
            let.save()
            return Response(let.data)


        return Response(flight_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 




