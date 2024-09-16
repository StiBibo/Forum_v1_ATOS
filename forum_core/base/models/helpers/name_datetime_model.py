from django.db import models
from .datetime_model import DatetimeModel

class NameDateTimeModel(DatetimeModel):
    name = models.CharField(max_length=255, null=True)

    class Meta : 
        abstract = True 

    def __str__(self):
        return self.name  