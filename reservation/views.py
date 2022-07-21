from rest_framework import viewsets, generics, status
from .serializers import PersonSerializer, ClientSerializer, RoomSerializer, ReservationSerializer #impor the serializer we just created
from .models import Person, Client, Reservation, Room
from rest_framework.response import Response
from django.http import JsonResponse, Http404
from rest_framework.views import APIView

class person_view_set(viewsets.ModelViewSet):
    # define queryset
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class client_view_set(viewsets.ModelViewSet):
    # define queryset
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class room_view_set(viewsets.ModelViewSet):
    # define queryset
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ReservationApiView(generics.ListCreateAPIView):
    """
        Busca por hash_reservation y/o id_reservation
    """
    queryset = Reservation.objects.all().order_by('id')
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = Reservation.objects.all()

        hash_reservation = self.request.query_params.get("hash_reservation")
        if hash_reservation is not None:
            queryset = queryset.filter(hash_reservation=hash_reservation)

        id_reservation = self.request.query_params.get('id')
        if id_reservation is not None:
            queryset = queryset.filter(id=id_reservation)

        return queryset.order_by('id')


    def post(self, request, *args, **kwargs):
        '''
            post reservations
        '''
        person_list = []
        room_list = []
        persons = request.data["persons"]

        for person in persons:
            try:
                c, new = Person.objects.get_or_create(**person)
                person_list.append(c.id)

                if not new:
                    print("Entry already in the DB:")
                    print(c)
            except:
                return JsonResponse(
                    status=status.HTTP_400_BAD_REQUEST, 
                    data ={'status':'false',
                           'message':"No hay suficientes datos de las persona",
                           'persons': f'{person}'
                    })

        numbers = request.data["room_ids"]
        for number in numbers:
            try:
                room_id = Room.objects.get(number=number["number"])

                if room_id:
                    room_list.append(room_id.id)
            except:
                return JsonResponse(
                    status=status.HTTP_400_BAD_REQUEST, 
                    data ={'status':'false',
                           'message':"Habitación no válida",
                           'room_ids': f'{number}'
                    })

        try:
            """
            si no encuenta el cliente no hace nada
            podría lanzar un error ?
            """
            if request.data["client_id"]:
                identification = request.data["client_id"]["identification"]
                client_id = Client.objects.get(identification=identification)
                if not client_id:
                    client_id = None
                    # return JsonResponse(
                    #     status=status.HTTP_400_BAD_REQUEST,
                    #     data ={'status':'false',
                    #         'message':"Cliente no válido",
                    #         'client_id': f'{identification}'
                    #     })
        except KeyError :
            client_id = None

        data = {
            'status': request.data.get('status'),
            'days': request.data.get('days'),
            'date_initial': request.data.get('date_initial'),
            'date_finished': request.data.get('date_finished'),
            'persons': person_list,
            'room_id': room_list,
            'client_id': client_id.id if client_id else None,
            'amount_total': request.data.get('amount_total'),
        }

        serializer = ReservationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                        status=status.HTTP_200_OK, 
                        data ={'status':'true',
                            'message':"Reserva realizada con éxito",
                            'reservation': serializer.data["id"],
                            'hash_reservation': serializer.data["hash_reservation"]
                        })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationListApiView(APIView):
    """
    get:
        Return a Reservation
    put:
        Update a Reservation
    delete:
        Delete a Reservation
    """
    def get_object(self, pk):
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        reservation = self.get_object(pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)