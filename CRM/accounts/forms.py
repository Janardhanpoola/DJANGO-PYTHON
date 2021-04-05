from django.forms import ModelForm
from .models import Order,Customer

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class CustomerSettingsForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user'] #we dont want customers to update the user info.

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User  # User model contains user details
        fields=['username','email','password1','password2'] #these fields are predefined in django

