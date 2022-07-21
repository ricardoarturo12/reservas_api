"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reservation.views import (
    person_view_set, client_view_set, 
    reservation_view_set,
    room_view_set, ReservationApiView)
from rest_framework import routers

# define the router
router = routers.DefaultRouter()
router.register(r'person', person_view_set)
router.register(r'client', client_view_set)
router.register(r'room', room_view_set)#t#the route tha will be used to access your API on the browser
router.register(r'reservation', reservation_view_set)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', ReservationApiView.as_view()),
    # Adds 'Login' link in the top right of the page

]