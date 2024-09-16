from django.db import models
from base.models.helpers.datetime_model import DatetimeModel
from .subject_model import SubjectModel

class MessageModel(DatetimeModel):
    sujet = models.ForeignKey(SubjectModel, on_delete=models.CASCADE, null=True)
    content = models.TextField()
