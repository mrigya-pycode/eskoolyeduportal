from django import forms
from .models import instituteinfo,Employeeinfo,Accountinfo
countrys = (
    ('india', 'china'),
    ('japan', 'uk'),
    ('usa', 'korea'),
    ('england', 'Manhattan'),
    ('poland', 'Staten Island'),
)
class instituteinfoform(forms.ModelForm):
    countrys = forms.ChoiceField(choices=countrys , required = True)
    class Meta:
        model=instituteinfo
        fields=['institute_name','institute_line','institute_logo','institute_number',
        'institute_web','institute_address','institute_country']


class rulesform(forms.ModelForm):
    class Meta:
        model=instituteinfo
        fields=['institute_rar']

class pfeesform(forms.ModelForm):
    class Meta:
        model=instituteinfo
        fields=['admission_fee','registration_fee','Art_material','Transport','Books','uniform','fine','others']

class Employeeinfoform(forms.ModelForm):
    class Meta:
        model=Employeeinfo
        fields=['emp_id','emp_type']

class accountinfoform(forms.ModelForm):
    class Meta:
        model=Accountinfo
        fields=["from_date","income_des","income_ammount","expense_ammount"]
