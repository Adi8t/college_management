from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate, login 



def home(request):
    return render(request, "home.html")

 
def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


def logout1(request):
    logout(request)
    return redirect('home')


def dashboard(request):
    return render(request, "principalsirpanel.html")


def signup(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cnfrm_password = request.POST.get("confirm_password")
        date_of_birth = request.POST.get("dateofbirth")

        if User.objects.filter(email=email).exists():
            context = {
                "error_message": "Email already exists."
            }
            return render(request, 'signup.html', context=context)

        if password == cnfrm_password:
            
            user, created = User.objects.get_or_create(email=email, username=name, date_of_birth=date_of_birth)
            if created:
                user.set_password(password)  
                user.save()
                login(request,user)
                return redirect('home')
        else:
            context = {
                "error_message": "Passwords do not match."
            }
            return render(request, 'signup.html', context=context)
    else:
        return render(request, 'signup.html')

def update_field(request):
    Teachers_all = User.objects.filter(role="teacher")
    context = {
        "teachers": Teachers_all
    }
    if Teachers_all != []:
        return render(request, 'teacherdata.html', context=context)
    else:
        context = {
            "error_message": "No Data available"
        }
        return render(request, 'teacherdata.html', context=context)


def update_teacher(request):
    if request.method == 'POST':
        if "update1" in request.POST:
            id = request.POST.get('id')
            username = request.POST.get('username')
            subject = request.POST.get('subject')
            email = request.POST.get('email')
            department=request.POST.get('dept')
            user = User.objects.get(id=id)
            user.username = username
            user.subject = subject
            user.email = email
            user.dept=department
            user.save()
            return redirect('update_field')
        elif "delete" in request.POST:
            id = request.POST.get('id')
            user = User.objects.get(id=id)
            user.delete()
            return redirect('update_field')
        elif "add" in request.POST:
            name = request.POST.get('name')
            subject = request.POST.get('subject')
            email = request.POST.get('email')
            dept = request.POST.get('dept') 
            if User.objects.filter(email=email).exists():
                return redirect('update_field')
            else:
                User.objects.get_or_create(username=name, email=email, subject=subject, dept=dept, role='teacher')
                return redirect('update_field')
    else:
        return render(request, 'teacherdata.html')

def student_field(request):
    studentall=User.objects.filter(role="student")

    context={
        "students":studentall
    }
    if studentall!=[]:
       return render(request,"studentdata.html",context=context)
    else:
        context={
            "error_message":"no student available"
        }
        return render(request,"studentdata.html",context=context)

def update_student(request):
    if request.method == 'POST':
        
        if "update" in request.POST:
            id = request.POST.get('id')
            username = request.POST.get('username')
            dept = request.POST.get('dept')
            email = request.POST.get('email')
            student = User.objects.get(id=id)
            student.username = username
            student.email = email
            student.dept = dept
            student.save()
            
            return redirect('update_student_field')
        elif "delete" in request.POST:
            id = request.POST.get('student_id')
            print(id)
            student = User.objects.get(id=id).delete()
           
            return redirect('update_student_field')
        if "add" in request.POST:
            name = request.POST.get('username')
            dept = request.POST.get('dept')
            email = request.POST.get('email')
            if User.objects.filter(email=email).exists():
                return redirect('update_student_field')
            else:
                student, created = User.objects.get_or_create(username=name,dept=dept,email=email)
                                                                   
                if created:
                    student.save()
                    return redirect('update_student_field')
    else:
        return render(request, 'studentdata.html')


def subject_field(request):
    subject_all = User.objects.filter(role="teacher")
    context = {
        "subjects": subject_all
    }
    if subject_all != []:
        return render(request, 'subjectdata.html', context=context)
    else:
        return render(request, 'subjectdata.html')   



def teacher_timetable(request):

    teachers = User.objects.filter(role='teacher')  

    context = {
        'teachers': teachers
    }

    return render(request, 'timetable.html', context)


