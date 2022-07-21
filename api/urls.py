from django.contrib import admin
from django.urls import path, include
from reservation.views import (
    person_view_set, client_view_set, 
    room_view_set, ReservationApiView,
    ReservationListApiView)
from rest_framework import routers

# define the router
router = routers.DefaultRouter()
router.register(r'person', person_view_set)
router.register(r'client', client_view_set)
router.register(r'room', room_view_set)#t#the route tha will be used to access your API on the browser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/reservation/', ReservationApiView.as_view()),
    path('api/reservation/<int:pk>/', ReservationListApiView.as_view(), name='reservations'),
]