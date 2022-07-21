from django.test import TestCase
from reservation.models import Client, Person, Room, Reservation


class PersonTestCase(TestCase):

    def setUp(self):
        Person.objects.create(identification="2879592",
                              name="Ricardo",
                              age=31)

    def test_string_method(self):
        person = Person.objects.get(id=1)
        expected_string = f"{person.name}"
        self.assertEqual(str(person), expected_string)


class ClientTestCase(TestCase):

    def setUp(self):
        Client.objects.create(identification="2879592",
                              name="Ricardo",
                              ruc="2879592-0")

    def test_string_method(self):
        client = Client.objects.get(id=1)
        expected_string = f"{client.name}"
        self.assertEqual(str(client), expected_string)


class RoomTestCase(TestCase):

    def setUp(self):
        Room.objects.create(number="10",
                            bed_qty=12,
                            price=40.0)

    def test_string_method(self):
        room = Room.objects.get(id=1)
        expected_string = f"{room.number}"
        self.assertEqual(str(room), expected_string)


class ReservationTestCase(TestCase):

    def setUp(self):
        person = Person.objects.create(
                            id=2,
                            identification="2879592",
                            name="Ricardo",
                            age=31)


        client = Client.objects.create(
                            id=2,
                            identification="2879592",
                            name="Ricardo",
                            ruc="2879592-0")

        room = Room.objects.create(
                            id=2,
                            number="10",
                            bed_qty=12,
                            price=40.0
                            )

        reservation = Reservation(
                            id=1,
                            status="pendiente",
                            days=12,
                            client_id=client,
                            date_initial= "2022-07-20T13:58:00Z",
                            date_finished= "2022-07-21T13:59:00Z",
                            amount_total=10000
                            )
        reservation.save()
        reservation.persons.add(person,)
        reservation.room_id.add(room,)

    def test_string_method(self):
        reservation = Reservation.objects.get(id=1)
        expected_string = f"{reservation.hash_reservation}"
        self.assertEqual(str(reservation), expected_string)

