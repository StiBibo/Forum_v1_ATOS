from django.db import models
from base.models.helpers.name_datetime_model import NameDateTimeModel

class MessageModel(NameDateTimeModel):

    subject = models.ForeignKey('api_rest.SubjectModel', on_delete=models.CASCADE, related_name="subject_ids")

    def __str__(self):
        return f"{self.name}"
    