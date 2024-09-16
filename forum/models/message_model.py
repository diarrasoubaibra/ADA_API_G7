from django.db import models
from forum.models.subject_model import SubjectModel

class MessageModel(models.Model):
    subject = models.ForeignKey(SubjectModel, related_name='subjects', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.subjecct.title