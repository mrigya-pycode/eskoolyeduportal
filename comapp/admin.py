from django.contrib import admin
from comapp.models import classes,subjects,instituteinfo,Studentsinfo,Employeeinfo
# Register your models here.
admin.site.register(classes)
admin.site.register(subjects)
admin.site.register(instituteinfo)
admin.site.register(Studentsinfo)
admin.site.register(Employeeinfo)
