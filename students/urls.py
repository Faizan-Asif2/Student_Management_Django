from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    #path('', views.home, name='home'),

    path('students/', views.student_list, name='student_list'),

    path(
        'students/<int:student_id>/',
        views.student_detail,
        name='student_detail'
    ),

    #path('about/', views.about, name='about'),
]