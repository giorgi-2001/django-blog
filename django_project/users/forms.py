from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, FileInput, EmailField
from .models import Profile, User


class UserRegisterForm(UserCreationForm):
    email = EmailField(
        required=True,
        max_length=150, 
        help_text=(
            "Required. 150 characters or fewer. "
            "Must be a valid email"
        ) 
    )
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

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