"""comproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from comapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.home,name="home"),
    path('login/', views.loginpage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
    path('studentdashboard/',views.studentdashboard, name="studentdashboard"),
    path('admindashboard/',views.admindashboard, name = "admindashboard"),
    path('teacherdashboard/',views.teacherdashboard, name = "teacherdashboard"),
    path('classview/',views.Classlistview.as_view(),name="classview"),
    path('Create/',views.Classcreateview.as_view()),
    path('Delete/<pk>',views.Classdelete.as_view()),
    path('Update/<pk>',views.Classupdate.as_view()),
    path('subCreate/',views.Subjectview,name="subCreate"),
    path('subadd/',views.Subjectaddview.as_view(),name="subadd"),
    path('Updatesub/<pk>',views.Subupdate.as_view()),
    path('instituteinfopage/<id>',views.instituteinfopage),
    path('allstudents/',views.allstudents,name="allstudents"),
    path('Studentcreateview/',views.Studentcreateview.as_view()),
    path('empview/',views.employeelistview.as_view(),name="empview"),
    path('empcreate/',views.Employeecreateview.as_view()),
    path('Deleteemp/<pk>',views.employeedelete.as_view()),
    path('Updateemp/<pk>',views.employeeupdate.as_view()),
    path('acccreate/',views.Accountcreateview.as_view()),    # path('',views..as_view()),
    path('incomecreate/',views.Incomecreateview.as_view()),
    path('expensecreate/',views.Expensecreateview.as_view()), 

]
