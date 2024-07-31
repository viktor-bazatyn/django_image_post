from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("email",)

    def __init__(self, *args, **kwargs):
        social_auth_data = kwargs.pop('social_auth_data', None)
        super().__init__(*args, **kwargs)
        if isinstance(social_auth_data, dict):
            self.fields['email'].initial = social_auth_data.get('email', '')


class AvatarForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar']
