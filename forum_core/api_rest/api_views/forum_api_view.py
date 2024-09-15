from rest_framework import viewsets
from api_rest.models.forum_model import ForumModel
from api_rest.serializers.forum_serializer import ForumSerializer







class ForumViewSet(viewsets.ModelViewSet):

    serializer_class = ForumSerializer
    queryset = ForumModel.objects.all()

