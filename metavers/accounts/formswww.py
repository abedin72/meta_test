from django import forms
from accounts.models import ProfileModel

class ProfileForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields=['Name','Email','Password']
       
class ProfileRegisterForm(forms.ModelForm):
    User_Name=models.CharField(max_length=100)
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Password=models.CharField()
    Email=models.CharField()
    

    class Meta:
        model=ProfileModel
        fields=['Name','Email','Password']
     