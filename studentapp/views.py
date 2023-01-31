from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from studentapp.forms import Stud_form, user_reg, mark_form, admin_form
from studentapp.models import Mark, Student_Registration


# Create your views here.
def home(request):

    return render(request,'index.html')

def log(request):

    return render(request,'login.html')

def stud_reg(request):
    u_form = user_reg()
    s_form = Stud_form()
    if request.method == 'POST':
        u_form = user_reg(request.POST)
        s_form = Stud_form(request.POST,request.FILES)
        if u_form.is_valid() and s_form.is_valid():
            user = u_form.save(commit=False)
            user.is_student = True
            user.save()
            student = s_form.save(commit=False)
            student.user = user
            student.save()
            messages.info(request, 'student registered successfully')
            return redirect('log')

    return render(request, 'stud_reg.html', {'u_form': u_form, 's_form': s_form})

def admin_reg(request):
    u_form = user_reg()
    a_form = admin_form()
    if request.method == 'POST':
        u_form = user_reg(request.POST)
        a_form = admin_form(request.POST, request.FILES)
        if u_form.is_valid() and a_form.is_valid():
            user = u_form.save(commit=False)
            user.is_admin = True
            user.save()
            admin = a_form.save(commit=False)
            admin.user = user
            admin.save()
            messages.info(request, 'student registered successfully')
            return redirect('log')

    return render(request, 'admin_reg.html', {'u_form': u_form, 'a_form': a_form})

def log(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user is not None and user.is_admin:
                return redirect('admin12')

            elif user is not None and user.is_student:
                 return redirect('student1')
        else:
            messages.info(request,'invalid credentials')

    return render(request,'login.html')

@login_required(login_url='log')
def admin12(request):
    return render(request,'admin.html')

@login_required(login_url='log')
def student1(request):
    return render(request,'student.html')

@login_required(login_url='log')
def add_mark(request):
    form = mark_form()
    if request.method == "POST":
        form = mark_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_admin_mark')
    return render(request, 'add_mark.html', {'form': form})

@login_required(login_url='log')
def view_admin_mark(request):
    data = Mark.objects.all()
    return render(request, 'view_admin_mark.html', {'data': data})

@login_required(login_url='log')
def view_student_mark(request):
    u = Student_Registration.objects.get(user=request.user)
    data = Mark.objects.filter(name=u)
    return render(request, 'view_student_mark.html', {'data': data})

@login_required(login_url='log')
def mark_update(request,id):
    fee1 = Mark.objects.get(id=id)
    form = mark_form(instance=fee1)
    if request.method =='POST' :
        form=mark_form(request.POST,instance = fee1)
    if form.is_valid():
        form.save()
        return redirect('view_admin_mark')
    return render(request,'add_mark.html',{'form':form})

@login_required(login_url='log')
def mark_delete(request,id):
    Mark.objects.get(id=id).delete()
    return redirect('view_admin_mark')

@login_required(login_url='log')
def view_profile(request):
    student = Student_Registration.objects.get(user=request.user)
    return render(request,'view_profile.html',{'student':student})

@login_required(login_url='log')
def view_profile(request):
    student = Student_Registration.objects.get(user=request.user)
    return render(request,'view_profile.html',{'student':student})

@login_required(login_url='log')
def profile_update(request):
    stud1 = Student_Registration.objects.get(user=request.user)
    form = Stud_form(instance=stud1)
    if request.method =='POST' :
        form=Stud_form(request.POST,request.FILES,instance = stud1)
    if form.is_valid():
        form.save()
        return redirect('view_profile')
    return render(request,'update_profile.html',{'form':form})

@login_required(login_url='log')
def view_admin_student(request):
    data = Student_Registration.objects.all()
    return render(request, 'view_admin_student.html', {'data': data})

@login_required(login_url='log')
def view_logout_student(request):
    logout(request)
    return redirect('log')

@login_required(login_url='log')
def view_logout_admin(request):
    logout(request)
    return redirect('log')