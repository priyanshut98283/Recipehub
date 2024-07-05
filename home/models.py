from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
# Above two imports is for django signals...

class Student(models.Model):
    id=models.IntegerField(primary_key=True) # auto id...
    name=models.CharField(max_length=100)
    age=models.IntegerField() # models.IntegerField(default=18)... for setting default value...
    email=models.EmailField()
    address=models.TextField()
    # image=models.ImageField() # need to install pillow for this...
    # file=models.FileField()
    # field=models.DateField()

    def __str__(self)->str:
        return self.name # this method will return name while showing details inside shell

class Products(models.Model):
    pass

"""  
Django signals are a way to run some methods on creation of objects... 
It can be used in some scenarios like when we add some data row-wise in database, save that to log
that who saved that data...

Types-> pre-save,post-save,pre-delete,post-delete

Implementation below->

"""

class Car(models.Model):
    car_name=models.CharField(max_length=100)
    speed=models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name

@receiver(post_save, sender = Car)
def call_car_api(sender,instance,**kwargs):
    print("Car object created!")
    print(sender , instance , kwargs)