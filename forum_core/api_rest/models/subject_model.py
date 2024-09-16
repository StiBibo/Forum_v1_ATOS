from django.db import models
from base.models.helpers.datetime_model import DatetimeModel
from .forum_model import ForumModel

class SubjectModel(DatetimeModel):
    forum = models.ForeignKey(ForumModel, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=255)

