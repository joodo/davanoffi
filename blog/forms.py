from django import forms
from blog.models import ContentImage

class ContentImageForm(forms.Form):
    title = forms.CharField(label='Title:', max_length=140)
    content = forms.ImageField()
