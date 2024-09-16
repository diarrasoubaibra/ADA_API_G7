from django.db import models
from forum.models.forum_model import ForumModel
from base.models.helpers.date_time_model import DateTimeModel


class SubjectModel(DateTimeModel):
    forum = models.ForeignKey(ForumModel, related_name='subjects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title