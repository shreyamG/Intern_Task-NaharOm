from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class AuthUser(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    
    SKILLS_CHOICES = (
        ('JS', 'JavaScript'),
        ('React', 'React'),
        ('API', 'API'),
        ('Backend', 'Backend'),
    )
    
    username = models.CharField(max_length=32, unique=True)
    # password = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # skills = models.CharField(max_length=50, choices = SKILLS_CHOICES)
    skills = models.ManyToManyField(Skill, related_name='users')
    
    def __str__(self):
        return self.username
    


