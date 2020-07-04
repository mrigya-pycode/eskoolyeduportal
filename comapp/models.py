from django.db import models

# Create your models here.
class classes(models.Model):
    class_name = models.CharField(max_length=500)
    class_monthly_fees = models.IntegerField()
    def __str__(self):
        return self.class_name

class subjects(models.Model):
    subject_name = models.CharField(max_length=500)
    subject_weightage = models.IntegerField()
    subclass_name = models.ForeignKey(classes, on_delete=models.CASCADE , default = "")
    def __str__(self):
        return self.subject_name


countrys = (
    ('india', 'china'),
    ('japan', 'uk'),
    ('usa', 'korea'),
    ('england', 'Manhattan'),
    ('poland', 'Staten Island'),
)

class instituteinfo(models.Model):
    institute_name = models.CharField(max_length=254)
    institute_line = models.CharField(max_length=300)
    institute_logo = models.FileField(upload_to='images/')
    institute_number = models.IntegerField()
    institute_web =  models.CharField(max_length=200)
    institute_address = models.CharField(max_length=400)
    institute_country = models.CharField(max_length=100,choices=countrys)
    institute_rar = models.CharField(max_length=800,default=" ")
    admission_fee = models.CharField(max_length=100,default=" ")
    registration_fee = models.CharField(max_length=100,default=" ")
    Art_material = models.CharField(max_length=300,default=" ")
    Transport = models.CharField(max_length=300,default=" ")
    Books = models.CharField(max_length=300,default=" ")
    uniform = models.CharField(max_length=300,default=" ")
    fine = models.IntegerField(default=" ")
    others = models.CharField(max_length=300,default=" ")
    def __str__(self):
        return self.institute_name


gender = (
    ('m', 'male'),
    ('f', 'female'),
    ('o', 'other'),
)

religion = (
    ('h', 'hindu'),
    ('m', 'muslim'),
    ('s', 'sikh'),
    ('g', 'gujrati'),
    ('c', 'cristian'),
    ('o', 'other'),
)

bg = (
    ('o', 'o+'),
    ('a+', 'A+'),
    ('ab+', 'AB+'),
    ('ab-', 'AB-'),
    ('o-', 'O-'),
    ('a-', 'A-'),
)

emptyp = (
    ('t', 'Teaching staff'),
    ('n', 'Non teaching staff'),

)



class Studentsinfo(models.Model):
    stu_name = models.CharField(max_length = 30, default = "")
    stu_regno = models.IntegerField(default = "")
    stu_classname = models.ForeignKey(classes, on_delete = models.CASCADE, default = "")
    stu_profile =  models.FileField(upload_to = "images/", null=True, blank=True, default = "ghgg")
    stu_admissiondate = models.DateField(default = "")
    stu_discount = models.IntegerField(default = "")
    stu_mobileno = models.IntegerField(default = "")
    stu_birthdate = models.DateField(null=True, blank=True, default = "")
    stu_orphan = models.BooleanField(null=True, blank=True, default = "")
    stu_gender = models.CharField(max_length = 20,choices = gender, null=True, blank=True, default = "")
    stu_caste =  models.CharField(max_length = 30, null=True, blank=True, default = "")
    stu_school =  models.CharField(max_length = 50, null=True, blank=True, default = "")
    stu_religion = models.CharField(max_length = 20,choices = religion,null=True, blank=True, default = "")
    stu_address = models.TextField(null=True, blank=True, default = "")
    stu_totalchildren =  models.IntegerField(null=True, blank=True, default = "")
    stu_fathername = models.CharField(max_length = 20,null=True, blank=True, default = "")
    stu_fatheroccupation = models.CharField(max_length = 20,null=True, blank=True, default = "")
    stu_fatheredu = models.CharField(max_length = 20,null=True, blank=True, default = "")
    stu_fatherincome = models.FloatField(null=True, blank=True, default = "")
    stu_fathermobile = models.IntegerField(null=True, blank=True, default = "")
    stu_mothername = models.CharField(max_length = 20,null=True, blank=True, default = "")
    stu_motheroccupation = models.CharField(max_length = 20,null=True, blank=True, default = "")
    stu_motheredu = models.CharField(max_length = 20,null=True, blank=True, default = "")
    stu_motherincome = models.FloatField(null=True, blank=True, default = "")
    stu_motehrmobile =models.IntegerField(null=True, blank=True, default = "")

class Employeeinfo(models.Model):
    emp_name = models.CharField(max_length = 30, default = "")
    emp_id = models.IntegerField(default = "")
    emp_joiningdate = models.DateField(null=True, blank=True, default = "")
    emp_type = models.CharField(max_length = 20,choices = emptyp , null=True, blank=True, default = "")
    emp_profile = models.FileField(upload_to = "images/", null=True, blank=True, default = "hhh")
    emp_mobileno = models.IntegerField(default = "")
    emp_salary = models.IntegerField(default = "")
    emp_fathersname = models.CharField(max_length = 20,null=True, blank=True, default = "")
    emp_experience_or_specilalization = models.CharField(max_length = 20,null=True, blank=True, default = "")
    emp_gender = models.CharField(max_length = 20,choices = gender, null=True, blank=True, default = "")
    emp_CNIC = models.CharField(max_length = 30, default = "")
    emp_email = models.CharField(max_length = 100, default = "")
    emp_rligion = models.CharField(max_length = 20,choices = religion,null=True, blank=True, default = "")
    emp_education = models.CharField(max_length = 100, default = "")
    emp_dob = models.DateField(null=True, blank=True, default = "")
    emp_bloodgroup =  models.CharField(max_length = 20,choices = bg,null=True, blank=True, default = "")
    emp_address = models.TextField(null=True, blank=True, default = "")

    def __str__(self):
        return self.emp_name

class Accountinfo(models.Model):
    from_date = models.DateField(null=True, blank=True, default = "")
    to_date = models.DateField(null=True, blank=True, default = "")


class Incomeinfo(models.Model):
    from_date = models.DateField(null=True, blank=True, default = "")
    income_des = models.CharField(max_length = 30, default = "")
    income_ammount = models.IntegerField(default = "")

class expenseinfo(models.Model):
    from_date = models.DateField(null=True, blank=True, default = "")
    expense_des = models.CharField(max_length = 30, default = "")
    expense_ammount = models.IntegerField(default = "")
