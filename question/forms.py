from django.core import validators
from django import forms
from .models import User

class Student(forms.ModelForm):
 class Meta:
  model = User
  fields = ['Ques', 'Answ']
  widgets = {
   'Ques': forms.TextInput(attrs={'class':'form-control'}),
   'Answ': forms.EmailInput(attrs={'class':'form-control'}),
   
  }