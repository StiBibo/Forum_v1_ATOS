from django.db import models

class DatetimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta :
        abstract = True