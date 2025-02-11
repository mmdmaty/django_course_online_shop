from django.forms import Form
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','email','age')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUserModel
        fields = UserChangeForm.Meta.fields 