from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.logout1, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("signup/", views.signup, name="signup"),
    path('update-teacher/', views.update_field, name='update_field'),
    path('update-teacher/update-teacher1/', views.update_teacher, name='update_teacher1'),
    path('update-student/', views.student_field, name='update_student_field'),
    path('update-student/update-student1/', views.update_student, name='update_student'),
    path("update-subject/", views.subject_field, name="update_subject"),
    path("table/", views.teacher_timetable, name="timetable")
]
