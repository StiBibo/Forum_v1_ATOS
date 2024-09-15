from rest_framework import serializers
from ..models.forum_model import ForumModel

class ForumSerialiizer(serializers.ModelSerializer):
    class Meta:
        model = ForumModel
        fields = "__all__"
