from django.db import models
from django.contrib.auth.models import AbstractUser 
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password




class Vital(models.Model):
    vital_connection= models.OneToOneField('Contact', related_name='vital_contact', on_delete= models.CASCADE)


class Contact(models.Model):
    name= models.CharField(max_length= 200, blank= False)
    number= PhoneNumberField(primary_key=True, default= None)
    email=models.EmailField(unique=True, blank= True)
    sitelinks= models.URLField(blank= True)
    date_of_birth= models.DateField(blank= True)
    vital_connection= models.BooleanField(default= False)

    class Meta:
        verbose_name= 'Contact'
        verbose_name_plural= 'Contacts'


    def __str__(self):
        return self.number + self.name[:8] 


class Individual(AbstractUser):
    contact= models.ForeignKey(Contact, on_delete= models.CASCADE, null= True)
    password= models.CharField(max_length=20, null= False, blank= False, validators=[validate_password], default= None)

    def __str__(self):
        return self.contact.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.contact.vital_connection== False:
            Vital.objects.create(vital_connection=self)







# Create your models here.
