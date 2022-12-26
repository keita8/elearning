from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from account.models import *
from django.conf import settings 

User = settings.AUTH_USER_MODEL

class Course(models.Model):
    name = models.TextField()
    year = models.IntegerField()
    
    class Meta:
        unique_together = ("name", "year", )
        verbose_name = 'Cours'
        verbose_name_plural = 'Cours'
        
    def __str__(self):
        return self.name


class Grade(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='Niveau')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Cours')
    
    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'
        
    def __str__(self):
        return f'{self.grade}'