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
from tinymce import models as tinymce_models


class UserManager(BaseUserManager):
    def create_user(
        self, email, password, is_admin, is_staff, is_active, **extra_fields
    ):
        if not email:
            raise ValueError("Users must have an email address")
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_admin=is_admin,
            is_active=is_active,
            last_login=now,
            date_joined=now,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, is_admin, is_active, is_staff, is_superuser, **extra_fields):
        return self._create_user(email, password, False, False, False, False, **extra_fields)

    def create_superuser(self, email, password, is_active, is_staff, is_superuser, is_admin, **extra_fields):
        user = self.create_user(email, password, True, True, True, True, **extra_fields)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        TEACHER = "TEACHER", "Enseignant(e)"
        STUDENT = "STUDENT", "Etudiant(e)"

    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)
    email = models.EmailField(max_length=254, unique=True, verbose_name="Adresse email")
    # name = models.CharField(max_length=254, null=True, blank=True, verbose_name="Nom d'utilisateur")
    is_staff = models.BooleanField(default=False, verbose_name="Staff")
    is_admin = models.BooleanField(default=False, verbose_name="Admin")
    is_active = models.BooleanField(default=False, verbose_name="Compte activé")
    last_login = models.DateTimeField(
        null=True, blank=True, verbose_name="Dernière connexion"
    )
    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name="Date d'inscription"
    )

    # the new user is teacher or student
    is_student = models.BooleanField(default=False, verbose_name="Etudiant ?")
    is_teacher = models.BooleanField(default=False, verbose_name="Enseignant ?")

    class Meta:
        verbose_name = "Compte"
        verbose_name_plural = "Comptes"

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)  # Call the real save() method

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


class Student(Account):
    base_role = Account.Role.STUDENT
    student = StudentManager()

    class Meta:
        proxy = True
        verbose_name = "Etudiant(e)"
        verbose_name_plural = "Etudiant(e)s"

    def welcome(self):
        return "Page étudiant"


class Teacher(Account):
    base_role = Account.Role.TEACHER
    teacher = TeacherManager()

    class Meta:
        proxy = True
        verbose_name = "Enseignant(e)"
        verbose_name_plural = "Enseignant(e)s"

    def welcome(self):
        return "Page enseignant"


class StudentProfile(models.Model):
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE, verbose_name="Adresse email"
    )
    lastname = models.CharField(max_length=100, verbose_name="Nom de famille")
    firstname = models.CharField(max_length=100, verbose_name="Prénom")
    birth_date = models.DateField(
        verbose_name="Date de naissance", default=timezone.now
    )
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name="Téléphone")
    bio = tinymce_models.HTMLField(blank=True, null=True)
    avatar = models.ManyToManyField(Image)

    class Meta:
        verbose_name = "Profil etudiant(e)"
        verbose_name_plural = "Profil etudiant(e)s"

    def __str__(self):
        return f"{self.user}"

    def __unicode__(self):
        return


@receiver(post_save, sender=Student)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "STUDENT":
        StudentProfile.objects.create(user=instance)


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE, verbose_name="Adresse email"
    )
    lastname = models.CharField(max_length=100, verbose_name="Nom de famille")
    firstname = models.CharField(max_length=100, verbose_name="Prénom")
    birth_date = models.DateField(
        verbose_name="Date de naissance", default=timezone.now
    )
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name="Téléphone")
    bio = tinymce_models.HTMLField(blank=True, null=True)
    avatar = models.ManyToManyField(Image)

    class Meta:
        verbose_name = "Profil enseignant(e)"
        verbose_name_plural = "Profil enseignant(e)s"

    def __str__(self):
        return f"{self.user}"

    def __unicode__(self):
        return


@receiver(post_save, sender=Teacher)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "TEACHER":
        TeacherProfile.objects.create(user=instance)
