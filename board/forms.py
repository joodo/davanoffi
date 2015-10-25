#!/usr/bin/env python
# encoding: utf-8

from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Tag


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '你的故事。'}), required=False)
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '描述和 Tags'}), required=False, max_length=140)
    music = forms.FileField(widget=forms.FileInput(attrs={'accept': 'audio/mpeg'}), required=False)
    image = forms.FileField(widget=forms.FileInput(attrs={'accept': 'image/*'}), required=False)

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image._size > 5*1024*1024:
                raise ValidationError('Image file should less then 5mb.')
            return image

    class Meta:
        model = Post
        fields = ['content', 'image', 'music', 'title', 'parent', ]


class TagForm(forms.ModelForm):
    background_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    content_text_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    title_text_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    anchor_text_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = Tag
        fields = ['background_color', 'content_text_color', 'title_text_color', 'anchor_text_color',]
