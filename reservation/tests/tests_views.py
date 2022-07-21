from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth import get_user_model
from reservation.models import Reservation, Room, Client, Person
import json


class AuthorsSerializerTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='testpass')
        self.client.force_authenticate(self.user)
        self.author_test = Person.objects.create(name='AuthorTest')


    def test_person_post(self):
        """Test create a new person"""
        payload = {
            "identification": "2879592",
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