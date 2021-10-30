from django.db import models
from django.contrib.auth.models import User

class QuisModel(models.Model):
    question = models.CharField(max_length=255, null=True)
    op1 = models.CharField(max_length=255, null=True)
    op2 = models.CharField(max_length=255, null=True)
    op3 = models.CharField(max_length=255, null=True)
    op4 = models.CharField(max_length=255, null=True)
    ans = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_user')

    def __str__(self) -> str:
        return self.question

