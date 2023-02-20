from django import forms
from accounts.models import ProfileModel


class UserRegisterForm(forms.Form):
    User_Name=forms.CharField(max_length=100)
    Email=forms.EmailField()
    Full_Name=forms.CharField(max_length=100)
    # Last_Name=forms.CharField(max_length=100)
    Password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    # Password2=forms.CharField(max_length=100,widget=forms.PasswordInput)
    


class ProfileRegisterForm(forms.ModelForm):
    username=forms.CharField(max_length=100)
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    password=forms.CharField()
    email=forms.CharField()
    

    class Meta:
        model=ProfileModel
        fields=['Full_Name','Email']
         