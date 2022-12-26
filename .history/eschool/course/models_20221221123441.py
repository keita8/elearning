from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    courses = models.ManyToManyField("Course", blank=True)

    class Meta:
        verbose_name_plural = "People"

class Course(models.Model):
    name = models.TextField()
    year = models.IntegerField()
    
    class Meta:

        verbose_name = 'Cours'
        verbose_name_plural = 'Courss'

    class Meta:

class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'