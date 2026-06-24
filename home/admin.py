from django.contrib import admin
from .models import Student  # Import your model
from django.contrib import admin
from django.db import models
from django.forms import TextInput
from import_export.admin import ImportExportModelAdmin
from .models import Student



class StudentAdmin(ImportExportModelAdmin):
    list_display=('name', 'email','admission_number','branch','year','contact_number','component_name','componentissue_date','componentdue_date','faculty_referred','remarks')
    list_editable=('remarks',)
    search_fields =('name','email','admission_number','branch','year')
    

    formfield_overrides={
        models.TextField: {'widget':TextInput(attrs={'style': 'width:150px; height:20px;'})}
    }

    
admin.site.register(Student, StudentAdmin)