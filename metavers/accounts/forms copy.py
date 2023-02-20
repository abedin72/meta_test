from django import forms

class UserRegisterForm(forms.Form):
    User_Name=forms.CharField(max_length=100)
    Email=forms.EmailField()
    First_Name=forms.CharField(max_length=100)
    Last_Name=forms.CharField(max_length=100)
    Password1=forms.CharField(max_length=100,widget=forms.PasswordInput)
    Password2=forms.CharField(max_length=100,widget=forms.PasswordInput)
    
    