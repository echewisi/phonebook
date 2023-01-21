from django.db import models
from django.contrib.auth.models import AbstractUser 




class Contact(models.Model):
    name= models.CharField(max_length= 200, blank= False)
    number= models.CharField(max_length=100, blank= True)
    email=models.EmailField(unique=True, blank= True)
    sitelinks= models.URLField(blank= True)
    date_of_birth= models.DateField(blank= True)
    vital_connection= models.BooleanField(default= False)

    def __str__(self):
        return self.name

    
    class Meta:
        ordering= ['name']

class Individual(AbstractUser):
    contacts= models.ForeignKey(Contact, related_name= 'contact_contacts', on_delete=models.CASCADE, null= True)



# Create your models here.
