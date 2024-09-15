from rest_framework import viewsets
from api_rest.models.subject_model import SubjectModel
from api_rest.serializers.subject_serializer import SubjectSerializer





class SubjectViewSet(viewsets.ModelViewSet):

    serializer_class = SubjectSerializer
    queryset = SubjectModel.objects.all()
