from tabnanny import verbose
from unittest import result
from weakref import proxy
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager, 
    PermissionsMixin)
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        TEACHER = "TEACHER", "Enseignant(e)"
        STUDENT = "STUDENT", "Etudiant(e)"
    
    base_role = Role.ADMIN
    role  = models.CharField(max_length=50, choices=Role.choices)
    email = models.EmailField(max_length=254, unique=True, verbose_name="Adresse email")
    name = models.CharField(max_length=254, null=True, blank=True, verbose_name="Nom d'utilisateur")
    is_staff = models.BooleanField(default=False, verbose_name="Staff")
    is_superuser = models.BooleanField(default=False, verbose_name="Super utilisateur")
    is_active = models.BooleanField(default=True, verbose_name="Compte activé")
    last_login = models.DateTimeField(null=True, blank=True, verbose_name="Dernière connexion")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")

    class Meta:
        verbose_name = 'Compte'
        verbose_name_plural = 'Comptes'
        
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs) # Call the real save() method
    
    def get_email(self):
        return f"{self.email}"

    def get_absolute_url(self):
        return f"{self.email}"
    
class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEACHER)
    
class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)
        
    
class Student(User):
    base_role = User.Role.STUDENT
    student = StudentManager()
    
    class Meta:
        proxy = True
        verbose_name = 'Etudiant(e)'
        verbose_name_plural = 'Etudiant(e)s'

    def welcome(self):
        return "Page étudiant"    
    
    
class Teacher(User):
    base_role = User.Role.TEACHER
    teacher = TeacherManager()
    
    class Meta:
        proxy = True
        verbose_name = 'Enseignant(e)'
        verbose_name_plural = 'Enseignant(e)s'
        
    def welcome(self):
        return "Page enseignant"