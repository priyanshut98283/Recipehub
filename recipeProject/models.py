from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.query import QuerySet 
# Above is default user model-> It has certain things like username,first_name... etc but not all...

# Now we can extend Abstract user class where we can use inbuilt models + we can define our own
# e.g. about or bio section on profile page,likes,dislikes etc...

# Now, if we want to use everything from scratch , write every model(variables) by ourself , 
# then we will extend abstract_base class...
# these are done in accounts app...

# Whenever we make any change here ,we need to migrate using->
# 1-> python manage.py makemigrations
# 2-> python manage.py migrate

# from django.contrib.auth import get_user_model
# User=get_user_model()
# above two lines code sets our own custom user model...


# Below code is custom model manager for is_deleted at every query...
class StudentManager(models.Manager):
    # def get_queryset(self) -> QuerySet:
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class Recipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    # For reference , on anything e.g. put curser on User inside ForeignKey 
    # and press ctrl + click , it will open its file location...

    recipe_name=models.CharField(max_length=100)
    recipe_description=models.TextField()
    recipe_image=models.ImageField(upload_to="recipe")

    # slug=models.SlugField(unique=True)
    
    # Suppose we deleted something and we want that in future we need to create , so we need 
    # to create backup for that and then delete , on need we can import that...
    # we call that soft delete... or lets suppose user deleted something and admin wants to know
    # logs that who deleted and why deleted...informations, then that data is invisible for users
    # but visible to admin...
    # For that scenario...we can make below is_deleted True...id data deleted ...and
    # In all files like views.py , change queryset=Recipe.objects.all() to
    # queryset=Recipe.objects.filter(is_deleted=False) ,now this will show data except deleted ones...
    # But we have huge files, doing this at all places will take much time...

    # For solving this issue , django provides model manager...

    # is_deleted=models.BooleanField(False)

    # Using above created custom model manager...

    # objects=RecipesManager()
    # admin_objects=models.Manager()

    # Implemented above id_deleted inside student class as it has more data...


class Department(models.Model):
    department=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering=['department']

    #  In above class, since ordering is true , it will store departments in ascending order...
    #  for descending put - sign ...

class StudentID(models.Model):
    student_id=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id

class Student(models.Model):
    department=models.ForeignKey(Department,related_name="depart",on_delete=models.CASCADE)
    # Here foreign key denotes one to many | many to one relationship...
    # e.g. one department can have many students | many students can belong to one department

    student_id=models.OneToOneField(StudentID,related_name="studentid",on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()

    is_deleted=models.BooleanField(default=False)

     # Using above created custom model manager...

    objects=StudentManager()
    admin_objects=models.Manager()

    """ 
    Now, inside shell , we can see all students via admin_objects but not via objects...as defined 
    above...
    >>> q=Student.objects.all()
    >>> q.count() # students filtered here where is_deleted =True
    140
    >>> q=Student.admin_objects.all() 
    >>> q.count()
    150


    >>> for s in q:
    ...  s.is_deleted=True
    ...  s.save()
    
    """

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering=['student_name']
        verbose_name="student"