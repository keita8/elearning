from rest_framework import serializers
from django.conf import settings
from .models import *

User = settings.AUTH_USER_MODEL


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(require=True)
    # firstname = serializers.SerializerMethodField()
    class Meta:
        model = StudentProfile
        fields = (
            "user",
            "sex",
            "lastname",
            "firstname",
            "birth_date",
            "phone_number",
            "bio",
        )

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop("user")
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student, created = StudentProfile.objects.update_or_create(
            user=user, lastname=validated_data.pop("lastname")
        )
        return student


class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ("phone_number",)


class UserTeacherUpdateSerializer(serializers.ModelSerializer):
    profile = TeacherProfileSerializer(source="teacherprofile", many=False)

    class Meta:
        model = Account
        fields = ("email", "profile")

        # Custom .update() method for serializer to handle UserProfile data update
        def update(self, instance, validated_data):
            userprofile_serializer = self.fields["profile"]
            userprofile_instance = instance.userprofile
            userprofile_data = validated_data.pop("teacherprofile", {})

            # to access the UserProfile fields in here
            # mobile = userprofile_data.get('mobile')

            # update the userprofile fields
            userprofile_serializer.update(userprofile_instance, userprofile_data)

            instance = super().update(instance, validated_data)
            return instance


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ("firstname", "lastname", "sex")
