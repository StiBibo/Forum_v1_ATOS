from django.db import models
from base.models.helpers.name_datetime_model import NameDateTimeModel


class ForumModel(NameDateTimeModel):
    description = models.CharField(max_length=255, null=True)
    
