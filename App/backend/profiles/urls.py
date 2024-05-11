from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.show_loginedstudent, name= 'show'),
    path('showstudent/<int:student_id>', views.show_student, name='showstudent' ),
    path('editstudent/<int:student_id>', views.edit_student, name='editstudent' ),
    path('edit/', views.edit_loginedstudent, name= 'edit'),
    path('update/', views.update_profile, name='update_profile'),
]
