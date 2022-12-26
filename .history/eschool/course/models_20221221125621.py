from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from account.models import *
from django.conf import settings 

User = settings.AUTH_USER_MODEL

class Course(models.Model):
    teacher = models.OneToOneField(Teacher, verbose_name="Enseignant", on_delete=models.CASCADE)
    name = models.CharField(max_length = 150, verbose_name='Matière', unique=True)
    year = models.IntegerField(verbose_name='Année')
    
    class Meta:
        unique_together = ("teacher", "name", 'year')
        verbose_name = 'Cours'
        verbose_name_plural = 'Cours'
        
    def __str__(self):
        return self.name


class Classe(models.Model):
    student = models.ManyToManyField(Student, related_name='students', verbose_name='Etudiants')
    course = models.ManyToManyField(Course, verbose_name="Matière")
    
    
    def __str__(self):
        return f" "

    def __unicode__(self):
        return 

    # person = models.ForeignKey(User, on_delete=models.CASCADE)
    # grade = models.PositiveSmallIntegerField(
    #     validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='Niveau')
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Cours')
    
    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'
        
    def __str__(self):
        return f'{self.grade}'