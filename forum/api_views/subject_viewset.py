from rest_framework import viewsets
from forum.models.subject_model import SubjectModel
from forum.serializers.subject_serializer import SubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer 