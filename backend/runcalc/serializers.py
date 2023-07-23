from rest_framework import serializers
from .models import Admin, User, Specialty

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
        
    def validate_email(self, value):
        """
        Check that the email is not already in use.
        """
        if Admin.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_email(self, value):
        """
        Check that the email is not already in use.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'
