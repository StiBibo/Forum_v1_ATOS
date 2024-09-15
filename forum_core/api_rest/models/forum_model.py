from django.db import models
from base.models.helpers.name_datetime_model import NameDateTimeModel


class ForumModel(NameDateTimeModel):

    def __str__(self):
        return f"{self.name}"
    