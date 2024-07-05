# Migration info->

""" 
Project create-> django-admin startproject mysite

Creating apps-> python manage.py startapp polls

Showing dependencies-> python -m pip freeze > requirements.txt

Migration->  python manage.py makemigrations
Migrate  ->  python manage.py migrate

Activating env->
go to env->Scripts->type ./activate in vscode and activate in command prompt

Creating virtualenv-> virtualenv env

Shell-> python manage.py shell or django-admin shell  

Runserver-> python manage.py runserver

Installing mysql-client-> pip3 install mysqlclient

Checking current user-> django-admin dbshell -- -c 'select current_user'

Builtin Template and Tags-> https://docs.djangoproject.com/en/5.0/ref/templates/builtins/

Sorting in shell-> 
Ascending->
>>> sortRecipe= Recipe.objects.all().order_by("recipe_name")
>>> sortRecipe
<QuerySet [<Recipe: Recipe object (1)>, <Recipe: Recipe object (10)>, <Recipe: Recipe object (3)>, <Recipe: Recipe object (9)>]>
>>>

Descending->
>>> sortRecipe= Recipe.objects.all().order_by("-recipe_name")
>>> sortRecipe
<QuerySet [<Recipe: Recipe object (9)>, <Recipe: Recipe object (3)>, <Recipe: Recipe object (10)>, <Recipe: Recipe object (1)>]>     
>>> 

1,10,3,9 becomes 9,3,10,1...

Now, for if records are much more like >10000,or 100000 then query can break...
So,put limit there->
Like for showing only 200 users->
>>> sortRecipe= Recipe.objects.all().order_by("recipe_name")[0:200] 

Now, if we have another schema in models.py -> e.g. likes 
and we want to show recipes who have >100 likes i.d. filter them->
Recipe.objects.filter(recipe_likes__gte=55).order_by("recipe_name")[0:200]
Above code will show first 200 recipes who have >=55 likes in ascending order ...

Here, __ is special operator and django checks that for applying that...
__gte means greater than and equal to...



"""

# Crud operations->
""" 
Insertions->
Open shell and write home.models import *
Way 1->
1) car= Car(name="suv",speed=110)
2) car.save()

Way 2->
1) Car.objects.create(name="suv",speed=110)

Way 3->
1) car_dict={"name":"suv","speed":110}
2) Car.objects.create(**car_dict)

Reading->
1) cars=Car.objects.all()
2) cars -> it will show all cars saved...

Other way to show->
s=Student.objects.all()  
for name in s:
... print(f"The name is {name.name} with age {name.age} with email {name.email} with address {name.address}")

Getting specific object->
car=Car.objects.get(id=1)
This method will throw error if there is no such id...

car=Car.objects.filter(id=1)
This method will not throw error if there is no such id instead will give empty object...

Updating->
1) First get object->
car= Car.objects.get(id=1)
then change->
car.name="new name"
car.speed="new speed"

car.save()

2) Also, 
Car.objects.filter(id=1).update(name="new name")


Deleting->

1) Deleting all records->
Car.objects.all().delete()

2) Deleting specific records->
Car.objects.get(id=1).delete()


"""