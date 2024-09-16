# viewset

from rest_framework import viewsets
from forum.models.forum_model import ForumModel
from forum.serializers.forum_serializer import ForumSerializer

class ForumViewSet(viewsets.ModelViewSet):
    queryset = ForumModel.objects.all()
    serializer_class = ForumSerializer 