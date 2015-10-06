from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Tag


class PostForm(forms.ModelForm):
    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image._size > 1024*1024:
                raise ValidationError('Image file should less then 1mb.')
            return image

    class Meta:
        model = Post
        fields = ['title', 'content', 'image']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['background_color', 'content_text_color', 'title_text_color', 'name']
