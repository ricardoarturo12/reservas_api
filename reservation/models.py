from django.db import models

import uuid


class Person(models.Model):
    identification = models.CharField(unique=True, 
                                      max_length=255)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Client(models.Model):
    identification = models.CharField(unique=True, 
                                      max_length=255)
    name = models.CharField(max_length=255)
    ruc = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.CharField(unique=True,
                              max_length=255)
    bed_qty = models.PositiveIntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.number


class Reservation(models.Model):

    STATUS = [
            ('pendiente',  'pendiente'),
            ('pagado', 'pagado'),
            ('eliminado', 'eliminado'),
    ]
    """Reservation object"""
    hash_reservation = models.UUIDField(default=uuid.uuid4, 
                                        editable=False)
    status = models.CharField(
        choices = STATUS,
        default ='pendiente',
        max_length=10
    )
    days = models.PositiveIntegerField()
    date_initial = models.DateTimeField()
    date_finished = models.DateTimeField()
    persons = models.ManyToManyField(Person)
    client_id = models.ForeignKey(
        'Client',
        on_delete = models.PROTECT,
        null = True
    )
    room_id = models.ManyToManyField(Room)
    amount_total = models.CharField(max_length=255, 
                                    null=True)

    def __str__(self):
        return f'{self.hash_reservation}'
