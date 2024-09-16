from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class ForumModel(DateTimeModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
