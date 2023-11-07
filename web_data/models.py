from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WebData(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField()
    phone_number = models.IntegerField()
    # MALE = "male"
    # FEMALE = "female"
    # OTHER = "other"
    # NONE ="none"
   
    # GENDER_CHOICES =[("NONE","none"),
    #          ("MALE","male"),
    #          ("FEMALE","female"),
    #          ("OTHER","other"),
             
     #        ]
    gender = models.CharField(max_length=20)


    def __str__(self):
        return self.username


    
