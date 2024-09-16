from django.db import models
from forum.models.subject_model import SubjectModel
from base.models.helpers.date_time_model import DateTimeModel


class MessageModel(DateTimeModel):
    subjecct = models.ForeignKey(SubjectModel, related_name='subjects', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self) -> str:
        return self.subjecct.title