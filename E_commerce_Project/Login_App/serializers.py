from rest_framework import serializers

from .models import Student

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     course = serializers.CharField()
#     city = serializers.CharField()
#     college = serializers.CharField()
#     email = serializers.EmailField()
#     date  = serializers.DateField()

#model Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student #attribute to class
        fields = ['name', 'course', 'city', 'college', 'email', 'date']