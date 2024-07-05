from django.shortcuts import render,redirect
from .models import * # importing models...
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q # for multiple filters and using pipe |
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# from django.contrib.auth import get_user_model
# User=get_user_model()
# above two lines code sets our own custom user model...

#  login module for session store ...and authenticate for password check-> entered password and 
#  stored encrypted password...and logout for logout of user...
@login_required(login_url="/login/") # this will make this route i.d. /recipes unable to access without login...
def recipes(request):
    if(request.method=="POST"):
        data=request.POST
        recipe_name=data.get("recipe_name")
        recipe_description=data.get("recipe_description")
        recipe_image=request.FILES.get("recipe_image")
        # print(recipe_name)
        # print(recipe_description)
        # print(recipe_image)
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        )

        return redirect('/recipes') # this will redirect to home page after saving data...
    
    queryset=Recipe.objects.all()

    if request.GET.get("search"): #another method to get data apart from data=request.POST
      queryset=queryset.filter(recipe_name__icontains=request.GET.get("search"))

    context={"recipes":queryset}

    return render(request,"recipes.html",context=context)

def termsAndConditions(request):
    return render(request,"termsAndConditions.html")

def delete_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    if request.user.is_superuser:
        queryset.delete()
        return redirect("/recipes/")
    else:
        messages.info(request, 'Only admin can delete!!')
        return redirect("/recipes/")

def update_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    context={"recipes":queryset}

    if request.method=="POST":
        data=request.POST

        recipe_name=data.get("recipe_name")
        recipe_description=data.get("recipe_description")
        recipe_image=request.FILES.get("recipe_image")
         
        queryset.recipe_name=recipe_name
        queryset.recipe_description=recipe_description
        if recipe_image:
            queryset.recipe_image=recipe_image
        
        queryset.save()

        return redirect("/recipes/")
        
    return render(request,"update_recipes.html",context)

def login_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request, 'Invalid username!!')
            return redirect("/login/")
        
        # if password==user.password this will not work as password is encrypted...
        user=authenticate(username=username,password=password)

        if user is None:
            messages.info(request, 'Invalid password!!')
            return redirect("/login/")
        
        else :
            login(request,user)
            return redirect("/recipes/")
        
    return render(request,"login.html")
    
    # if both username and password is correct we are putting it in session->
    #  In session, for every page user is not going to login again and again ...
    #  Until logout, he can use all functionalities on any page...
    #  all storage,session can be seen inside inspect-> application->left panel...

def logout_page(request):
    logout(request)
    return redirect("/login/")

def register_page(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=User.objects.filter(username=username)
        # user=User.objects.filter(username=username | first_name=first_name) 

        if user.exists():
            messages.info(request, 'User already exists! Enter another username!!')
            return redirect("/register/")

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            # password=password -> this will save password without encryption...
        )

        user.set_password(password) # this will save encrypted password...
        # ctrl + click on set_password then ctrl + click on make_password to open hashers.py file where 
        # salt and encryption is there...
        user.save()

        """ 
         shell output->

          >>> from django.contrib.auth.models import * 
          >>> User.objects.all()
          <QuerySet [<User: priyanshut123>, <User: priyanshut987>, <User: priyanshut546>]>

        """

        return redirect("/register/")

    return render(request,"register.html")