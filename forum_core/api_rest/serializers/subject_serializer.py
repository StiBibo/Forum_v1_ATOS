from rest_framework import serializers
from ..models.subject_model import SubjectModel

class SubjectSerializer(serializers.ModelSerializer):
    class Meta :
        model = SubjectModel
        fields = "__all__"
