from django.forms import ModelForm, FileInput
from .models import Profile, User


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
        widgets = {
            "image": FileInput(attrs={
                "class": "image-input",
            })
        }


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["username"]