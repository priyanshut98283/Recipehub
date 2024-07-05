from faker import Faker
fake=Faker()
import random
from .models import *

# Faker is a python library to get fake data...

# Below -> syntax means it is returning None...
def seed_db(n=10) -> None:
    try:
        for _ in range(n):
            # [1,2,3,4]
            departments_objs=Department.objects.all()
            random_index=random.randint(0,len(departments_objs)-1)
            department=departments_objs[random_index]
            student_id=f'STU-0{random.randint(0000,9999)}'
            student_name=fake.name()
            student_email=fake.email()
            student_age=random.randint(18,22)
            student_address=fake.address()

            student_id_obj=StudentID.objects.create(student_id=student_id)

            student_obj=Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
            )
    except Exception as e:
        print(e)

