from django.contrib import admin
from .models import Student  # Import your model


class StudentAdmin(admin.ModelAdmin):

    list_display=('name', 'email','admission_number','branch','year','contact_number','component_name','componentissue_date','componentdue_date','faculty_referred')

admin.site.register(Student,StudentAdmin)  # Register the model