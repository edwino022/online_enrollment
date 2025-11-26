from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [

    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),

    path('dashboard/', views.dashboard, name="dashboard"),


    path("students/", views.view_student, name="view_student"),
    path("students/add/", views.add_student, name="add_student"),
    path("students/edit/<int:pk>/", views.edit_student, name="edit_student"),
    path("students/delete/<int:pk>/", views.delete_student, name="delete_student"),

    path('subjects/', views.view_subject, name='view_subject'),
    path('subjects/add/', views.add_subject, name='add_subject'),
    path('subjects/edit/<int:pk>/', views.edit_subject, name='edit_subject'),
    path('subjects/delete/<int:pk>/', views.delete_subject, name='delete_subject'),

    # SCHEDULES
    path('schedules/', views.view_schedule, name='view_schedule'),
    path('schedules/add/', views.add_schedule, name='add_schedule'),
    path('schedules/edit/<int:pk>/', views.edit_schedule, name='edit_schedule'),
    path('schedules/delete/<int:pk>/', views.delete_schedule, name='delete_schedule'),

    # ENROLLMENTS
    path('enrollments/', views.view_enrollment, name='view_enrollment'),
    path('enrollments/add/', views.add_enrollment, name='add_enrollment'),
    path('enrollments/edit/<int:pk>/', views.edit_enrollment, name='edit_enrollment'),
    path('enrollments/delete/<int:pk>/', views.delete_enrollment, name='delete_enrollment'),

    path('logout/', views.logout_view, name='logout'),

]
