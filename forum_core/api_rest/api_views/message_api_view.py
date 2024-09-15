from rest_framework import viewsets
from api_rest.models.message_model import MessageModel
from api_rest.serializers.message_serializer import MessageSerializer





class MessageViewSet(viewsets.ModelViewSet):

    serializer_class = MessageSerializer
    queryset = MessageModel.objects.all()

