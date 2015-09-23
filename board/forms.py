from django import forms

from .models import Post

class ContentImageForm(forms.Form):
    title = forms.CharField(label='Title:', max_length=140)
    content = forms.ImageField()
