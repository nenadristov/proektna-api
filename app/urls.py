from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name = 'home'),
   path('api/create-passenger/', views.Create_passenger, name = "Create_passenger"),
   path('api/create-flight/', views.Create_flight, name = "Create_flight"),
   path('api/get-all-passengers/', views.get_all_passengers, name = 'get_all_passengers'),
   path('api/get-passenger-by-id/<int:pk>/', views.get_passenger_by_id, name = 'get_passenger_by_id'),
   path('api/get-all-flights/', views.get_all_flights, name = 'get_all_flights'),
   path('api/get-flight-by-id/<int:pk>/', views.get_flights_by_id, name = 'get_flights_by_id')



   #path('api/create-flight', views.Create_flight, name = "Create_flight"),
   

]