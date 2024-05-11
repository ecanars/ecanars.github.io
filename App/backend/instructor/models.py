from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length = 30)
    password = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.name)
    
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.JSONField(blank=True, null=True)
    
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    prompt = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    category = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.prompt)
    
    @classmethod
    def create(cls, prompt, answer, category, difficulty):
        return cls.objects.create(prompt=prompt, answer=answer, category=category, difficulty=difficulty)
    
class Assessment(models.Model):
    assessment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=20)
    questions = models.ManyToManyField(Question)
    
    @classmethod
    def create(cls, name, course):
        return cls.objects.create(name=name, course=course)
    
    @classmethod
    def update(cls, self, questions):
        self.questions.add(*questions)
        return self

