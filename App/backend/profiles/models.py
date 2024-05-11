from django.db import models
from instructor.models import Assessment

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='userprofile')
    id_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    department = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    assesments = models.ManyToManyField(Assessment, blank=True)
    
    # Course ve Grade modeli eklenince burayı aç!
    #courses = models.ManyToManyField(Course, blank=True)    
    #grades = models.ManyToManyField(Grade, blank=True)
    

    def __str__(self):
        return f"{self.name} ({self.id_number})"
    
    @classmethod
    def create(cls, user, id_number, name, email, department, year):
        return cls.objects.create(user=user, id_number=id_number, name=name, email=email, department=department,year=year)
