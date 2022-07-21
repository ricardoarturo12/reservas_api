from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth import get_user_model
from reservation.models import Reservation, Room, Client, Person
import json


class PersonSerializerTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='testpass')
        self.client.force_authenticate(self.user)
        self.person_test = Person.objects.create(
            identification= "test",
            name= "Soledad Molinas",
            age= 31,
        )


    def test_person_post(self):
        """Test create a new person"""
        payload = {
            "identification": "test1",
            "name": "Soledad Molinas",
            "age": 31,
        }

        response = self.client.post("/person/",
                                    payload,
                                    format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        exists = Person.objects.filter(
                identification=payload['identification']
        ).exists()
        self.assertTrue(exists)


    def test_person_get(self):
        """Test get person"""
        response = self.client.get("/person/",
                                    format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        exists = Person.objects.all().exists()
        self.assertTrue(exists)


    def test_person_put(self):
        """Test put a person"""
        payload = {
            'identification': 'test12',
            'name': 'Nombre de test',
            'age': 23,
        }
        response = self.client.put(f'/person/{self.person_test.id}/' ,
                                   data=payload,
                                   format='json')
        self.assertEqual(status.HTTP_200_OK,
                         response.status_code)

        exists = Person.objects.filter(
                identification=payload['identification']
        ).exists()
        self.assertTrue(exists)


    def test_person_delete(self):
        """Test delete a person"""
        payload = {
            'identification': 'test12',
            'name': 'Nombre de test',
            'age': 23,
        }
        response = self.client.delete(f'/person/{self.person_test.id}/' ,
                                   data=payload,
                                   format='json')
        self.assertEqual(status.HTTP_204_NO_CONTENT,
                         response.status_code)


class ReservationSerializerTestCase(APITestCase):
    pass