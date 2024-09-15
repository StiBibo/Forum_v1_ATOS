from django.db import models
from base.models.helpers.name_datetime_model import NameDateTimeModel

class SubjectModel(NameDateTimeModel):
    forum = models.ForeignKey('api_rest.ForumModel', on_delete=models.CASCADE, related_name="forum_ids")

    def __str__(self):
        return f"{self.name}"