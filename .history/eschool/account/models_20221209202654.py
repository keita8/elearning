from tabnanny import verbose
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
    role  = models.CharField(max_length=50, choices=Role.choices, default=base_role)
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
    
    def get_email(self):
        return f"{self.email}"

    def get_absolute_url(self):
        return f"{self.email}"
    
    
class Student(User):
    def __init__(self, *args):
        super(Student, self).__init__(*args)
        