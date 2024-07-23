from rest_framework import serializers
from .models import User
from authentication.serializers import UserSerializer
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)  # Use None as default value
        if user_data:
            user = User.objects.create_user(**user_data)
        else:
            raise serializers.ValidationError({'user': 'This field is required.'})
        student = Student.objects.create(user=user, **validated_data)
        return student
