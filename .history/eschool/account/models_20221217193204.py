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
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user


# class User(AbstractBaseUser):
#     class Role(models.TextChoices):
#         ADMIN = "ADMIN", "Admin"
#         TEACHER = "TEACHER", "Enseignant(e)"
#         STUDENT = "STUDENT", "Etudiant(e)"

#     base_role = Role.STUDENT
#     role = models.CharField(max_length=50, choices=Role.choices)
#     email = models.EmailField(
#         verbose_name='adresse email',
#         max_length=255,
#         unique=True,
#     )
#     is_active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False) # a admin user; non super-user
#     admin = models.BooleanField(default=False) # a superuser
#     last_login = models.DateTimeField(
#         null=True, blank=True, verbose_name="Dernière connexion"
#     )
#     date_joined = models.DateTimeField(
#         auto_now_add=True, verbose_name="Date d'inscription"
#     )

#     # the new user is teacher or student
#     is_student = models.BooleanField(default=False, verbose_name="Etudiant ?")
#     is_teacher = models.BooleanField(default=False, verbose_name="Enseignant ?")

#     # notice the absence of a "Password field", that is built in.

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = [] # Email & Password are required by default.
#     objects = UserManager()

#     def get_full_name(self):
#         # The user is identified by their email address
#         return self.email

#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.email

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         return self.staff

#     @property
#     def is_admin(self):
#         "Is the user a admin member?"
#         return self.admin
    
    
#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.role = self.base_role
#             return super().save(*args, **kwargs)  # Call the real save() method





class User(AbstractBaseUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        TEACHER = "TEACHER", "Enseignant(e)"
        STUDENT = "STUDENT", "Etudiant(e)"

    base_role = Role.STUDENT
    role = models.CharField(max_length=50, choices=Role.choices)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin




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
        verbose_name = "Etudiant(e)"
        verbose_name_plural = "Etudiant(e)s"

    def welcome(self):
        return "Page étudiant"


class Teacher(User):
    base_role = User.Role.TEACHER
    teacher = TeacherManager()

    class Meta:
        proxy = True
        verbose_name = "Enseignant(e)"
        verbose_name_plural = "Enseignant(e)s"

    def welcome(self):
        return "Page enseignant"


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Adresse email"
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
        User, on_delete=models.CASCADE, verbose_name="Adresse email"
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
