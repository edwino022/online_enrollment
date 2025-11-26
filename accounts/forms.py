from django import forms
from .models import Student, Subject, Schedule, Enrollment


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email_address', 'section','year', 'department']



class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['code', 'name']


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['subject', 'day', 'time', 'room']


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'schedule', 'subject','id','action',]
