from django.db import models
from forum.models.forum_model import ForumModel

class SubjectModel(models.Model):
    forum = models.ForeignKey(ForumModel, related_name='subjects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title