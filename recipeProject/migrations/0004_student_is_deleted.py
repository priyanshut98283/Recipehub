# Generated by Django 4.2.5 on 2023-12-27 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeProject', '0003_department_studentid_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
