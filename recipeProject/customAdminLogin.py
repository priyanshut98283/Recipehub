"""  
Follow steps to make custom fields like phone_number or email instead of username to login in admin
page...

Step 1->
Create custom userclass and use AbstractUser | AbstractBaseUser class...
as done in models.py in accounts app...

Step 2->
Make custom manager as created manager.py in accounts app...
Define the two methods-> def create_user() and def create_superuser()...
as done in manager.py in accounts app...

Step 3->
Write below line code in settings.py...
AUTH_USER_MODEL='accounts.CustomUser'

Step 4->
Write below code where we are using models as done in recipeProject-> views.py and models.py ...

from django.contrib.auth import get_user_model
User=get_user_model()
# above two lines code sets our own custom user model...

Step 5->
Create superuser with phone_number first...

delete db.sqlite3 or database we have used ... like delete or rename django database we are using...
or create backup of data or do this at start of project...
study about this more...other options to do this...
Make migrations using ->
python manage.py makemigrations
python manage,py migrate

Run->
python manage.py runserver and login to admin page...
Done!

Everything above written is commented in files...

"""