from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.TextField()
    email = models.EmailField()
    admission_number = models.TextField()
    branch = models.TextField()
    year = models.IntegerField()
    contact_number = models.BigIntegerField()
    component_name = models.TextField()
    componentissue_date = models.TextField()
    componentdue_date = models.TextField()
    faculty_referred = models.TextField()
    remarks =models.TextField(blank=True, null=True, help_text="Remarks")

    class Meta:
        db_table = 'students'  # This forces the table name to be 'students'
