from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_eventstream import send_event


from .models import Room, Participant, Offer, Answer, IceCandidate
from .serializers import RoomSerializer, ParticipantSerializer, OfferSerializer, AnswerSerializer, \
    IceCandidateSerializer


class CreateRoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class JoinRoomView(generics.CreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = ParticipantSerializer(data={"room": kwargs.get("room_id")})

        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateOfferView(generics.CreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)
        offer = serializer.instance

        # send event to the target user
        send_event(
            'user-{}'.format(offer.target.user.id),
            'new-offer',
            {'message': 'New offer received', 'offer_id': offer.id}
        )


class CreateAnswerView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)
        answer = serializer.instance

        send_event(
            'user-{}'.format(answer.caller.user.id),
            'new-answer',
            {'message': 'New answer received', 'answer_id': answer.id}
        )


class CreateIceCandidateView(generics.CreateAPIView):
    queryset = IceCandidate.objects.all()
    serializer_class = IceCandidateSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)
        ice_candidate = serializer.instance

        send_event(
            f'user-{ice_candidate.target.user.id}',
            'new-ice-candidate',
            {
                'message': 'New ICE candidate received',
                'ice_candidate_id': ice_candidate.id,
                'candidate': ice_candidate.candidate,
                'sdp_mid': ice_candidate.sdp_mid,
                'sdp_mline_index': ice_candidate.sdp_mline_index
            }
        )
