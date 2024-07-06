from django import forms
from .models import Post, Image


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': False, 'required': False}),
        }
