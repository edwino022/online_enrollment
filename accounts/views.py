from django.shortcuts import render, redirect
from .models import Student, Subject, Schedule, Enrollment
from .forms import StudentForm, SubjectForm, ScheduleForm, EnrollmentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("accounts:dashboard")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            from django.contrib.auth.models import User
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, "Account created! You can now log in.")
                return redirect("accounts:login")

    return render(request, "accounts/register.html")






def dashboard(request):
    # Make sure user is authenticated
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    return render(request, 'accounts/dashboard.html')



def view_student(request):
    students = Student.objects.all()
    return render(request, "accounts/view_student.html", {"students": students})

def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("accounts:view_student")
    return render(request, "accounts/add_student.html", {"form": form})

# EDIT STUDENT
def edit_student(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('accounts:view_student')

    return render(request, 'accounts/edit_student.html', {'form': form})

# DELETE STUDENT
def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect("accounts:view_student")  # ✅ correct

    return render(request, 'accounts/delete_student.html', {'student': student})

def view_subject(request):
    subjects = Subject.objects.all()
    return render(request, "accounts/view_subject.html", {"subjects": subjects})

def add_subject(request):
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('accounts:view_subject')
    return render(request, "accounts/add_subject.html", {"form": form})

def edit_subject(request, pk):
    subject = Subject.objects.get(id=pk)
    form = SubjectForm(request.POST or None, instance=subject)
    if form.is_valid():
        form.save()
        return redirect('accounts:view_subject')
    return render(request, 'accounts/edit_subject.html', {'form': form})

def delete_subject(request, pk):
    subject = Subject.objects.get(id=pk)
    if request.method == "POST":
        subject.delete()
        return redirect('accounts:view_subject')
    return render(request, 'accounts/delete_subject.html', {'subject': subject})




# SCHEDULES
def view_schedule(request):
    schedules = Schedule.objects.all()
    return render(request, 'accounts/view_schedule.html', {'schedules': schedules})



def add_schedule(request):
    form = ScheduleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('accounts:view_schedule')
    return render(request, "accounts/add_schedule.html", {"form": form})

def edit_schedule(request, pk):
    schedule = Schedule.objects.get(id=pk)
    form = ScheduleForm(request.POST or None, instance=schedule)
    if form.is_valid():
        form.save()
        return redirect('accounts:view_schedule')
    return render(request, 'accounts/edit_schedule.html', {'form': form})

def delete_schedule(request, pk):
    schedule = Schedule.objects.get(id=pk)
    if request.method == "POST":
        schedule.delete()
        return redirect('accounts:view_schedule')
    return render(request, 'accounts/delete_schedule.html', {'schedule': schedule})

# ENROLLMENTS
def view_enrollment(request):
    enrollments = Enrollment.objects.all()
    return render(request, "accounts/view_enrollment.html", {"enrollments": enrollments})


def add_enrollment(request):
    form = EnrollmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("accounts:view_enrollment")
    return render(request, "accounts/add_enrollment.html", {"form": form})

def edit_enrollment(request, pk):
    enrollment = Enrollment.objects.get(id=pk)
    form = EnrollmentForm(request.POST or None, instance=enrollment)
    if form.is_valid():
        form.save()
        return redirect('accounts:view_enrollment')
    return render(request, 'accounts/edit_enrollment.html', {'form': form})

def delete_enrollment(request, pk):
    enrollment = Enrollment.objects.get(id=pk)
    if request.method == "POST":
        enrollment.delete()
        return redirect('accounts:view_enrollment')
    return render(request, 'accounts/delete_enrollment.html', {'enrollment': enrollment})


def logout_view(request):
    logout(request)
    return redirect("accounts:login")

