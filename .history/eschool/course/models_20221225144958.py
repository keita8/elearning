from curses import savetty
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.db import models
from django.conf import settings
from account.models import upload_image_path_course, upload_image_path_video, upload_image_path_pdf, Teacher, Student
from datetime import datetime
from rest_framework import serializers
import uuid
from tinymce.models import HTMLField
from django.utils.text import slugify



User = settings.AUTH_USER_MODEL


class Standard(models.Model):
    name = models.CharField(max_length = 150, unique=True, verbose_name='Classe')
    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))
    year = models.DateTimeField(verbose_name='Année académique', auto_now_add= True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    description = HTMLField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            return super(Standard, self).save(*args, **kwargs) # Call the real save() method
    
    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'
    
    def __str__(self):
        return f"{self.name}"
    
    
class Subject(models.Model):
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, verbose_name='Classe', related_name='standards')
    subject_id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, verbose_name='Cours')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, editable=False)
    description = HTMLField()
    image = models.ImageField(upload_to=upload_image_path_course, blank=True, null=True)
    
    def save(self, *args, **kwargs):
           if not self.slug:
               self.slug = slugify(self.subject_id)
               return super(Subject, self).save(*args, **kwargs) # Call the real save() method
    
    class Meta:
        verbose_name = 'Cours'
        verbose_name_plural = 'Cours'
        
    def __str__(self):
        return self.name
    
    
class Lesson(models.Model):

    lesson_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    instructor = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Professeur', related_name='instructor')
    standard = models.ForeignKey(Standard, verbose_name='Classe', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, verbose_name='Cours', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True, verbose_name='Titre de la leçon')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, editable=False)
    grade = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)], verbose_name='Chapitre', blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    video = models.URLField()
    # video =  models.FileField(upload_to=upload_image_path_video, verbose_name='contenu vidéo', blank=True, null=True,  validators=[FileExtensionValidator( ['mp4'] ) ])
    pdf = models.FileField(upload_to=upload_image_path_pdf, null=True, blank=True, validators=[FileExtensionValidator( ['pdf'] ) ])
    note = models.FileField(upload_to=upload_image_path_pdf, null=True, blank=True, validators=[FileExtensionValidator( ['pdf', 'ppt', 'docs', 'xls'] ) ])
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Date de publication')
    
    def save(self, *args, **kwargs):
           if not self.slug:
               self.slug = slugify(self.lesson_id)
               return super(Lesson, self).save(*args, **kwargs) # Call the real save() method
    
    class Meta:
        ordering = ('grade', )
        verbose_name = 'Leçon'
        verbose_name_plural = 'Leçons'
        
    def __str__(self):
        return f"{self.name}"