from django.shortcuts import render,redirect,get_object_or_404
from comapp.models import classes,subjects,instituteinfo,Studentsinfo,Employeeinfo,Accountinfo,Incomeinfo,expenseinfo
from comapp.forms import instituteinfoform,rulesform,pfeesform,Employeeinfoform
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
#from EskoolyApp.models import Student,Teacher,Admin
from django.contrib.auth.models import User
#from EskoolyApp.forms import AdminLogin,StudentLogin,TeacherLogin
#from .decorators import unauthenticated_user, allowed_users,admin_only
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView



# Create your views here.

def home(request):
    return render(request,'comapp/home.html');

def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('uname')
        password=request.POST.get('psw')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Page redirection for admin after login
            if request.user.is_superuser:
                return HttpResponseRedirect('/admindashboard/')
            # Page redirection for teacher after login
            elif request.user.is_staff:
                return HttpResponseRedirect('/teacherdashboard/')
            # Page redirection for student after login
            else:
                return HttpResponseRedirect('/studentdashboard/')
        else:
            return HttpResponse('Error Generated')
            # messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request,'comapp/login.html')

def logoutUser(request):
	logout(request)
	return redirect('home')

def studentdashboard(request):
    return render(request, 'comapp/studentdashboard.html')

def admindashboard(request):
    print('*'*50,'In Admin Dashboard')
    return render(request,'comapp/admindashboard.html')

def teacherdashboard(request):
    return render(request, 'comapp/teacherDash.html')



class Classlistview(ListView):
    model = classes

class Classcreateview(CreateView):
    model = classes
    fields='__all__'

    def get_success_url(self):
        return reverse("classview")

class Classupdate(UpdateView):
    model = classes
    fields='__all__'

    def get_success_url(self):
        return reverse("classview")



class Classdelete(DeleteView):
    model = classes
    def get_success_url(self):
        return reverse("classview")


def Subjectview(request):
    return render(request,"comapp/Subjectcreate.html",{'classes' : classes.objects.all()})


class Subjectaddview(CreateView):
    model = subjects
    fields='__all__'

    def get_success_url(self):
        return reverse("subCreate")


class Subupdate(UpdateView):
    model = classes
    fields='__all__'

    def get_success_url(self):
        return reverse("classview")


def instituteinfopage(request,id):
     obj = get_object_or_404(instituteinfo,id=id)
     obj1 = get_object_or_404(instituteinfo,id=id)
     obj2 = get_object_or_404(instituteinfo,id=id)
     info = instituteinfo.objects.all()
     list1=instituteinfoform();
     list2=rulesform();
     list3=pfeesform();
     mdict1={'list1':list1,'info':info,'list2':list2,'list3':list3}
     if request.method == 'POST':
         list1=instituteinfoform(request.POST,request.FILES, instance = obj);
         list2=rulesform(request.POST, instance = obj1)
         list3=pfeesform(request.POST, instance = obj2)
         if list1.is_valid():
             obj=list1.save()
             obj.save()
             mydict1 = {'list1':list1,'info':info,'list2':list2,'list3':list3}
         if list2.is_valid():
             obj1 = list2.save()
             obj1.save()
             mydict1 = {'list1':list1,'info':info,'list2':list2,'list3':list3}
         if list3.is_valid():
             obj2 = list3.save()
             obj2.save()
             mydict1 = {'list1':list1,'info':info,'list2':list2,'list3':list3}
     return render(request,'comapp/instituteinfopage.html',context=mdict1);


def allstudents(request):
        return render(request, 'comapp/studentinfopage.html', {'Studentsinfo': Studentsinfo.objects.all()})


class Studentcreateview(CreateView):
    model = Studentsinfo
    fields='__all__'

    def get_success_url(self):
        return reverse('comapp/studentinfopage.html')


# def allemployees(request,id):
#      obj = get_object_or_404(Employeeinfo,id=id)
#      empinfo = Employeeinfo.objects.all()
#      list1=Employeeinfoform();
#      mdict1={'list1':list1,'empinfo':empinfo}
#      if request.method == 'POST':
#          list1=Employeeinfoform(request.POST,request.FILES, instance = obj);
#          if list1.is_valid():
#              obj=list1.save()
#              obj.save()
#      return render(request, 'comapp/Employeeinfopage.html',context=mdict1)
#
# class Employeecreateview(CreateView):
#     model = Employeeinfo
#     fields='__all__'
#
#     def get_success_url(self):
#         return reverse('comapp/Employeeinfopage.html')



class employeelistview(ListView):
    model = Employeeinfo

class Employeecreateview(CreateView):
    model = Employeeinfo
    fields='__all__'

    def get_success_url(self):
        return reverse("empview")

class employeeupdate(UpdateView):
    model = Employeeinfo
    fields='__all__'

    def get_success_url(self):
        return reverse("empview")

class employeedelete(DeleteView):
    model = Employeeinfo
    def get_success_url(self):
        return reverse("empview")


class Accountcreateview(CreateView):
    model = Accountinfo
    fields='__all__'

    def get_success_url(self):
        return reverse("accview")

class Incomecreateview(CreateView):
    model = Incomeinfo
    fields='__all__'

    def get_success_url(self):
        return reverse("accview")

class Expensecreateview(CreateView):
    model = expenseinfo
    fields='__all__'

    def get_success_url(self):
        return reverse("accview")
