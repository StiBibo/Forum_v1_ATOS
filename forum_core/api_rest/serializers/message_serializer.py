from rest_framework import serializers
from ..models.message_model import MessageModel

class MessageSerialiizer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = "__all__"