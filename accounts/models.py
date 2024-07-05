from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

# Creating custom class-> Having inbuilt models + our own...
# Import AbstractBaseUser for creating fully custom class...

# class CustomUser(AbstractUser):
#     username=None # this is written as we are now trying to login to admin page by email/phone not username...
#     phone_number=models.CharField(max_length=100,unique=True)
#     email=models.EmailField(unique=True)
#     user_bio=models.CharField(max_length=50)
#     user_profile_image=models.ImageField(upload_to="profile")

#     USERNAME_FIELD='phone_number' # this means use phone_number to login instead of username...

    # Now, when we run create superuser command...it doesn't get our custom names like email...
    # for that we need to write our own manager that how these fields will be save...

