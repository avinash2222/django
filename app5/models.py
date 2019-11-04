from django.db import models
from django.forms import ModelForm
# Create your models here.

class FormName(models.Model):
    name=models.CharField(max_length=12)
    email=models.EmailField()
    text=models.CharField(max_length=12)

class FormModel(ModelForm):
    class Meta:
        model = FormName
        fields = '__all__'
