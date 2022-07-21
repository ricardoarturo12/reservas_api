from rest_framework import viewsets
from .serializers import PersonSerializer, ClientSerializer, RoomSerializer, ReservationSerializer #impor the serializer we just created
from .models import Person, Client, Reservation, Room
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
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

class reservation_view_set(viewsets.ModelViewSet):
    # define queryset
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationApiView(APIView):
    def post(self, request, *args, **kwargs):
        '''
            post items
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