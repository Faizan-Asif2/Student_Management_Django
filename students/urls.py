# students/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),                 # /students/
    path('about/', views.about, name='about'),                         # /students/about/
    path('<int:student_id>/', views.student_detail, name='student_detail'),  # /students/5/
    path('home/', views.home, name='home'),
    path('course/<str:course_code>/',views.course_detail,name='course_detail'),
    path('<int:student_id>/marks/<int:marks>/',views.student_marks,name='student_marks'),
]