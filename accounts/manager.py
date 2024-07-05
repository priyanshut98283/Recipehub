# from django.contrib.auth.base_user import BaseUserManager

# class UserManager(BaseUserManager):
#     #  We need to modify two methods -> for running createsuperuser command...

#     def create_user(self,phone_number,password=None,**extra_fields):
#         if not phone_number:
#             raise ValueError("Phone number is required...")
        
#         extra_fields["email"]=self.normalize_email(extra_fields["email"])
#         user=self.model(phone_number=phone_number,**extra_fields)
#         user.set_password(password)
#         user.save(using=self.db)

#         return user
    
#     def create_superuser(self,phone_number,password=None,**extra_fields):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_superuser',True)
#         extra_fields.setdefault('is_active',True)

#         return self.create_superuser(phone_number,password,**extra_fields)