"""
URL configuration for firstDjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# importing home

from home.views import *
from recipeProject.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # for staticfiles...
from home.utils import *

urlpatterns = [
    path('admin/', admin.site.urls),

    #Home response ->
    path('',home,name="home"),

    path('contact/',contact,name="contact"),

    # If about is in another directory home , we need to write home/about here as django only understands
    # templates directory as default...
    path('about/',about,name="about"),

    # Recipes page->
    path('recipes/',recipes,name="recipes"),

    path('delete-recipes/<id>/',delete_recipe,name="delete_recipes"),

    path('update-recipes/<id>/',update_recipe,name="update_recipes"),

    path('login/',login_page,name="login_page"),

    path('logout/',logout_page,name="logout_page"),

    path('register/',register_page,name="register_page"),

    path('termsAndConditions/',termsAndConditions,name="termsAndConditions"),

    path('send_email/',send_email,name="send_email"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()