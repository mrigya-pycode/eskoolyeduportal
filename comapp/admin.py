from django.contrib import admin
from comapp.models import classes,subjects,instituteinfo,Studentsinfo,Employeeinfo,Accountinfo
# Register your models here.
admin.site.register(classes)
admin.site.register(subjects)
admin.site.register(instituteinfo)
admin.site.register(Studentsinfo)
admin.site.register(Employeeinfo)
admin.site.register(Accountinfo)
# admin.site.register(Incomeinfo)
# admin.site.register(Expenseinfo)
