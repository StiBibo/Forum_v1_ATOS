from django.db import models
from base.models.helpers.name_datetime_model import NameDateTimeModel
from .subject_model import SubjectModel

class MessageModel(NameDateTimeModel):
    # Relation between subject and message
    sujet = models.ForeignKey(SubjectModel, on_delete=models.CASCADE, null=True)
    content = models.TextField()
