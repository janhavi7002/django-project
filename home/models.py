from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

    email = models.EmailField()

    admission_number = models.CharField(max_length=30)

    branch = models.CharField(max_length=50)

    year = models.IntegerField()

    contact_number = models.CharField(max_length=10)

    component_name = models.CharField(max_length=100)

    componentissue_date = models.DateField()

    componentdue_date = models.DateField()

    faculty_referred = models.CharField(max_length=100)

    class Meta:
        db_table = 'students'