from rest_framework import serializers
from api_rest.models.forum_model import ForumModel


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumModel
        fields = "__all__"