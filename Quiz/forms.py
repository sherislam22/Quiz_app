from django.db.models import fields
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class AddQuestionform(ModelForm):
    class Meta:
        model = QuisModel
        fields = "__all__"
        