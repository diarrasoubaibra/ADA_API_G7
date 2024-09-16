from rest_framework import viewsets
from forum.models.message_model import MessageModel
from forum.models.subject_model import SubjectModel
from forum.serializers.message_serializer import MessageSerializer
from rest_framework.response import Response


class MessageViewSet(viewsets.ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer 

    def list(self, request):
        id = request.GET.get('subject')
        
        if id is None:
            subject = MessageModel.objects.all()
            serializer = MessageSerializer(subject, many=True)
            return Response(serializer.data)
        else:
            subject = MessageModel.objects.filter(subject=id)
            serializer = MessageSerializer(subject, many=True)
            return Response(serializer.data)