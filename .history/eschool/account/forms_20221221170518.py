from dataclasses import field, fields
from django import forms
from django.conf import settings
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = settings.AUTH_USER_MODEL

User = get_user_model()


class UserLoginForm(forms.ModelForm):
    """UserRegistrationForm definition."""

    email = forms.EmailField(
        label="Adresse email",
        widget=forms.EmailInput(
            attrs={"placeholder": "Votre adresse email", "required": True}
        ),
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Mot de passe", "required": True}
        ),
    )

    class Meta:
        model = User
        fields = ("email", "password")


class RegisterForm(forms.ModelForm):
    """
    The default

    """

    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmez", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email"]

    def clean_email(self):
        """
        Verify email is available.
        """
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError(
                "Cette adresse email est deja associée à un autre compte."
            )
        return email

    def clean(self):
        """
        Verify both passwords match.
        """
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("password_2")
        if password1 is not None and password1 != password2:
            self.add_error("Les mots de passe ne correspondent pas.")
        return cleaned_data


class UserAdminCreationForm(UserCreationForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """

    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmation")

    class Meta:
        model = User
        fields = ["email"]

    def clean(self):
        """
        Verify both passwords match.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password is not None and password != password2:
            raise ValueError("Les mots de passe ne correspondent pas.")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "password", "is_active"]

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class TeacherProfileForm(forms.ModelForm):
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Votre prénom"}),
        label="Prénom"
    )
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Votre nom"}),
        label='Nom'
    )
    sex = forms.ChoiceField(
        widget=forms.Choice(attrs={"placeholder": "Genre"}),
        label="Genre"
    )
    gender = forms.ChoiceField(label='', choices=SEX, widget=forms.Select(attrs={'class':'regDropDown'}))

    class Meta:
        model = TeacherProfile
        fields = (
            "user",
            "sex",
            "course",
            "lastname",
            "firstname",
            "birth_date",
            "phone_number",
            "bio",
            "image",
        )
        exclude = ("user",)
