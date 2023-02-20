from django.db import models   
from django.contrib.auth.models import User  
    
# Create your models here.
class ProfileModel (models.Model):
    class Meta :
        verbose_name="user"
        verbose_name_plural="user"
    user=models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="user",related_name="profile")
    Full_Name=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100,null=True)
    # status_chioces=((Man,"mmmmm"),(Woman,"wwww"))
    # Gender=models.IntegerField(choices=status_chioces)
    ProfileImage=models.ImageField(default='00-default.jpg',upload_to="ProfileImages/")
    # def __str__(self):
    #     return self.Full_Name
        # return "Ful_Name:{} {}".format(Name,Family)