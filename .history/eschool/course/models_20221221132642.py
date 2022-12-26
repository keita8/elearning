from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
from account.models import *

User = settings.AUTH_USER_MODEL

class Course(models.Model):
    # teacher = models.OneToOneField(Teacher, verbose_name="Enseignant", on_delete=models.CASCADE)
    name = models.CharField(max_length = 150, verbose_name='Matière', unique=True)
    year = models.IntegerField(verbose_name='Année')

        
    def __str__(self):
        return self.name
    
    @property
    def get_courses(self):
        return self.cours.all()


class Classe(models.Model):
    teacher = models.ManyToManyField("account.Model", verbose_name=_(""))
    student = models.ManyToManyField('account.Student', related_name='students', verbose_name='Etudiants')
    course = models.ManyToManyField(Course, verbose_name="Matière", related_name='cours')
    
    

    # person = models.ForeignKey(User, on_delete=models.CASCADE)
    # grade = models.PositiveSmallIntegerField(
    #     validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='Niveau')
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Cours')
    
    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'
        
    def __str__(self):
        return f'{self.course.name}'