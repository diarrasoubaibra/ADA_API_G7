from rest_framework import viewsets
from forum.models.message_model import MessageModel
from forum.serializers.message_serializer import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer 