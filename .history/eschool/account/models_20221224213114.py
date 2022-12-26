from tabnanny import verbose
from versatileimagefield.placeholder import OnDiscPlaceholderImage
import os
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from upload.models import Image
from tinymce.models import HTMLField
from course.models import *
from versatileimagefield.fields import VersatileImageField, PPOIField
from django.core.validators import (
    FileExtensionValidator,
    MinValueValidator,
    MaxValueValidator,
)
import os
import random
import string


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910207878)
    name, ext = get_filename_ext(filename)
    final_filename = f"{new_filename}{ext}"
    return f"profile/avatar/{new_filename}/{final_filename}"


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_admin, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError("L'adresse email est obligatoire")
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_admin=is_admin,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, True, **extra_fields)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "ADMIN"
        STUDENT = "STUDENT", "ETUDIANT"
        TEACHER = "TEACHER", "ENSEIGNANT"

    base_role = Role.ADMIN
    role = models.CharField(
        max_length=20, choices=Role.choices, verbose_name="Fonction"
    )
    email = models.EmailField(max_length=254, unique=True)
    # name = models.CharField(max_length=254, null=True, blank=True)
    is_student = models.BooleanField(default=False, verbose_name="etudiant")
    is_teacher = models.BooleanField(default=False, verbose_name="enseignant")
    is_staff = models.BooleanField(default=False, verbose_name="staff")
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False, verbose_name='admin')
    is_active = models.BooleanField(default=True, verbose_name="compte deja activé ?")
    last_login = models.DateTimeField(
        default=timezone.now, verbose_name="dernière connexion"
    )
    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name="date d'inscription"
    )

    class Meta:
        verbose_name = "Compte"
        verbose_name_plural = "Comptes"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
    
    @property
    def get_email(self):
        return self.email
    
    def has_module_perms(self, app_label: str) -> bool:
        return True

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
    
    def has_perm(self, perm: str, obj= None) -> bool:
        return self.is_admin
    

class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=Account.Role.TEACHER)


class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=Account.Role.STUDENT)


class Student(Account):
    base_role = Account.Role.STUDENT
    student = StudentManager()

    class Meta:
        proxy = True
        verbose_name = "Etudiant"
        verbose_name_plural = "Etudiant"

    def welcome(self):
        return "Page étudiant"


class Teacher(Account):
    base_role = Account.Role.TEACHER
    teacher = TeacherManager()

    class Meta:
        proxy = True
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignant"

#     def welcome(self):
#         return "Page enseignant"


class StudentProfile(models.Model):
    class Gender(models.TextChoices):
        HOMME = "Mr", "Mr"
        FEMME = "Mme", "Mme"

    gender = Gender.HOMME
    sex = models.CharField(max_length=20, null=True, blank=True, choices=Gender.choices, verbose_name="Genre")
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE, verbose_name="Adresse email"
    )
    lastname = models.CharField(max_length=100, verbose_name="Nom de famille", default='')
    firstname = models.CharField(max_length=100, verbose_name="Prénom", default='')
    birth_date = models.DateField(
        verbose_name="Date de naissance", default=timezone.now
    )
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name="Téléphone")
    bio = HTMLField(blank=True, null=True)
    avatar = models.ImageField(
        "Photo de profil",
        upload_to=upload_image_path,
        # ppoi_field="image_ppoi",
        validators=[FileExtensionValidator(["jpg", "png"])],
    )

    image_ppoi = PPOIField()

    class Meta:
        verbose_name = "Profil etudiant"
        verbose_name_plural = "Profil etudiant"

    def __str__(self):
        return f"{self.user}"

    def __unicode__(self):
        return


@receiver(post_save, sender=Student)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "STUDENT":
        StudentProfile.objects.create(user=instance)


class TeacherProfile(models.Model):

    class Gender(models.TextChoices):
        HOMME = "Mr", "Mr"
        FEMME = "Mme", "Mme"

    gender = Gender.HOMME
    sex = models.CharField(max_length=20, null=True, blank=True, choices=Gender.choices, verbose_name="Genre")
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE, verbose_name="Adresse email"
    )
    course = models.ManyToManyField(Course, verbose_name="Matière dispensée")
    lastname = models.CharField(max_length=100, verbose_name="Nom de famille")
    firstname = models.CharField(max_length=100, verbose_name="Prénom")
    birth_date = models.DateField(
        verbose_name="Date de naissance", default=timezone.now
    )
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name="Téléphone")
    bio = HTMLField(blank=True, null=True)
    image = models.ImageField(
        "Photo de profil",
        upload_to=upload_image_path,
        # ppoi_field="image_ppoi",
        validators=[FileExtensionValidator(["jpg", "png"])],
    )
    height = models.PositiveIntegerField("Image Height", blank=True, null=True)
    width = models.PositiveIntegerField("Image Width", blank=True, null=True)
    image_ppoi = PPOIField()

    class Meta:
        verbose_name = "Profil enseignant"
        verbose_name_plural = "Profil enseignant"

    def __str__(self):
        return f"{self.user}"

    def __unicode__(self):
        return


@receiver(post_save, sender=Teacher)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "TEACHER":
        TeacherProfile.objects.create(user=instance)

print(help(TeacherProfile))