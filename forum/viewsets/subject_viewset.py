from rest_framework import viewsets
from forum.models.subject_model import SubjectModel
from forum.serializers.subject_serializer import SubjectSerializer
from rest_framework.response import Response 

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer 

    def list(self, request):
        id = request.GET.get('forum')
        
        if id is None:
            forum = SubjectModel.objects.all()
            serializer = SubjectSerializer(forum, many=True)
            return Response(serializer.data)
        else:
            forum = SubjectModel.objects.filter(forum=id)
            serializer = SubjectSerializer(forum, many=True)
            return Response(serializer.data)