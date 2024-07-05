""" 
Django Queries->

>>> from recipeProject.models import *

1->
>>> query=Student.objects.filter(student_name__startswith="A") 
>>> query
<QuerySet [<Student: Alexa Green>, <Student: Alexander Harrison>, <Student: Allison Allen>,
<Student: Amy Smith>, <Student: Annette Shaw>, <Student: Ashley Davis>, <Student: Ashley Dunlap>]>

2->
>>> query1=Student.objects.filter(student_email__endswith = ".org" ) 
>>> query1
<QuerySet [<Student: Allison Allen>, <Student: Annette Shaw>, <Student: Ashley Dunlap>,
 <Student: Brandi Rojas>, <Student: Brent Stark>, '...(remaining elements truncated)...']>

3->
>>> for q in query1: 
...  print(q.student_email)
...
cindy70@example.org
llyons@example.org
oellis@example.org...

4->
>>> query1=Student.objects.filter(student_email__icontains = ".org" ) 
>>> query1                  
<QuerySet [<Student: Allison Allen>, ...]>

5->
>>> query1[0].id //details of first student...
110
>>> query1[0].pk
110
Here, django has default pk which means primary key which is usually same as id...

6->
>>> query1[0].department
<Department: Computer Science> // returning class of department here...
>>> query1[0].department.department
'Computer Science'             // returning department here...
Here , if we have any date_of_establish in class Department...we can access it through
>>> query1[0].department.department.date_of_establish

7->
>>> query=Student.objects.filter(department__department = "Civil" )   
>>> query        
<QuerySet [<Student: Chad Burns>,]>
Here, __ is a special operator that django understands , it can be used to call functions,
use other functions like icontains,endswith...and accessing foreign key...

8->
>>> query=Student.objects.filter(department__department = "Civil" )
>>> query.count()
21

9->
>>> dpts=["Civil","Electrical"]
>>> query=Student.objects.filter(department__department__in = dpts )    
>>> query.count()
36

10->
>>> query=Student.objects.exclude(department__department = "Civil" ) 
>>> query.count()
129

>>> query.exists() 
True

>>> len(query)    
129

>>> query[0:2]  
[<Student: Alexa Green>, <Student: Alexander Harrison>]

>>> query.values()
<QuerySet [{'id': 50, 'department_id': 6, 'student_id_id': 50, 'student_name': 'Chad Burns', 'student_email': 'mburke@example.net', 'student_age': 21, 'student_address': '79824 Fisher Mountains\nLisaside, OK 61485'}, ...]>

>>> query[0]
<Student: Chad Burns>

>>> query.values()[0]
{'id': 50,
 'department_id': 6,
 'student_id_id': 50,
 'student_name': 'Chad Burns',
 'student_email': 'mburke@example.net',
 'student_age': 21, 
 'student_address': '79824 Fisher Mountains\nLisaside, OK 61485'
}

>>> query.values()[0]["student_age"] 
21
Since its a dict now...we cannot use . operator as its not an object or class anymore...

>>> query=Student.objects.filter(department__department = "Civil" )     
>>> query.values().reverse()
Above query will show reverse data...

>>> query=Student.objects.values_list('id','student_name')              
>>> query
<QuerySet [(73, 'Alexa Green'),'...(remaining elements truncated)...']>


11->
>>> query=Student.objects.get(id=101)                        
>>> query
<Student: Luis Washington>
Above get method throws exception if there is no data found...be aware...

Aggregation-> These queries works on a single column ... e.g. finding count(),average(),max(),min()
etc... in a column

Annotation-> These queries works on multiple columns , like we can use multiple aggregate 
functions with annotate...

These queries directly give results...

Aggregate->

>>> from django.db.models import *
Above line will import all avg(),max(),min()... functions...

12->
>>> Student.objects.aggregate(Avg('student_age'))
{'student_age__avg': 20.0}

>>> Student.objects.aggregate(Max('student_age')) 
{'student_age__max': 22}

>>> Student.objects.aggregate(Min('student_age')) 
{'student_age__min': 18}

>>> Student.objects.aggregate(Sum('student_age')) 
{'student_age__sum': 3000}

Annotate->
>>> student=Student.objects.values('student_age').annotate(Count('student_age'))
>>> student
<QuerySet [{'student_age': 19, 'student_age__count': 29}, {'student_age': 22, 
'student_age__count': 34}, {'student_age': 18, 'student_age__count': 34}, 
{'student_age': 21, 'student_age__count': 29}, {'student_age': 20, 'student_age__count': 24}]>


>>> student=Student.objects.values('department').annotate(Count('department'))   
>>> student
<QuerySet [{'department': 1, 'department__count': 27}, {'department': 2, 'department__count': 15},
 {'department': 3, 'department__count': 31}, {'department': 4, 'department__count': 21}, 
 {'department': 5, 'department__count': 15}, {'department': 6, 'department__count': 21}, 
 {'department': 7, 'department__count': 20}]>

Above code means department 1 has 27 students and so on...

>>> student=Student.objects.values('department','student_age').annotate(Count('department'),Count('student_age')) 
>>> student
<QuerySet [{'department': 4, 'student_age': 19, 'department__count': 3, 'student_age__count': 3}, '...(remaining elements truncated)...']>



"""