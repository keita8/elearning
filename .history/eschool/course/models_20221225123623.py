from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.db import models
from django.conf import settings
from account.models import *
from datetime import datetime
from rest_framework import serializers
import uuid
from eschool.account.models import upload_image_path


User = settings.AUTH_USER_MODEL


class Course(models.Model):
    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    instructor = models.ForeignKey(
        Teacher,
        verbose_name="Enseignant",
        on_delete=models.CASCADE,
        related_name="course",
    )
    name = models.CharField(max_length=150, verbose_name="Matière", unique=True)
    year = models.IntegerField(verbose_name="Année", choices=year_choice)

    class Meta:
        verbose_name = "Cours"
        verbose_name_plural = "Cours"

    def __str__(self):
        return self.name


class Classe(models.Model):
    name = models.CharField(max_length=150, verbose_name="Classe", unique=True)
    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    start = models.IntegerField(choices=year_choice, verbose_name="Début d'année")
    end = models.IntegerField(choices=year_choice, verbose_name="Fin d'année")
    # teacher = models.ManyToManyField("account.Teacher", verbose_name="enseignants")
    student = models.ManyToManyField(
        "account.Student", related_name="students", verbose_name="Etudiants"
    )

    # person = models.ForeignKey(User, on_delete=models.CASCADE)
    # grade = models.PositiveSmallIntegerField(
    #     validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='Niveau')
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Cours')

    class Meta:
        verbose_name = "Classe"
        verbose_name_plural = "Classes"

    def __str__(self):
        return f"{self.name}"


class Standard(models.Model):
    name = models.CharField(max_length = 150)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'
    
    def __str__(self):
        return f"{self.name}"
    
    
class Subject(models.Model):
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, verbose_name='Classe')
    subject_id = models.CharField(max_length=10)
    name = models.CharField(max_length=200, verbose_name='Cours')
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='cours', blank=True)
    
    class Meta:
        verbose_name = 'Cours'
        verbose_name_plural = 'Cours'
        
    def __str__(self):
        return self.name
    
    
class Lesson(models.Model):
    lesson_id = models.UUIDField(primary_key=True, editable=False, unique=True)
    standard = models.ForeignKey(Standard, verbose_name='Classe', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, verbose_name='Cours', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True, verbose_name='Titre de la leçon')
    slug = models.SlugField(max_length=100, unique=True)
    grade = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)], verbose_name='Chapitre', blank=True, null=True)
    video =  models.FieldFile(upload_to=upload_image_path_video, verbose_name='contenu vidéo', blank=True, null=True,  validators=[FileExtensionValidator( ['mp4'] ) ])
    pdf = models.FileField(upload_to=upload_image_path_pdf, null=True, blank=True, validators=[FileExtensionValidator( ['pdf'] ) ])
    note = models.FileField(upload_to=upload_image_path_pdf, null=True, blank=True, validators=[FileExtensionValidator( ['pdf', 'ppt', 'docs', 'xls'] ) ])
    instructor = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Professeur', related_name='instructor')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Date de publication')
    
    class Meta:
        ordering = ('-')
        verbose_name = 'Leçon'
        verbose_name_plural = 'Leçons'