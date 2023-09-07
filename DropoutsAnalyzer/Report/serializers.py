from rest_framework import serializers
from .models import School, Student, Dropout


class SchoolSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = School
        fields = ['name', 'city', 'state']

class StudentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Student
        fields = '__all__'


class DropoutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dropout
        fields = '__all__'


class FilterSerializer_state(serializers.Serializer):
    state = serializers.CharField(source='student__school__state')
    student_count = serializers.IntegerField()

    # def state(self):
    #     return self.student__school__state

class FilterSerializer_city(serializers.Serializer):
    city = serializers.CharField(source='student__school__city')
    student_count = serializers.IntegerField()


class FilterSerializer_school(serializers.Serializer):
    school = serializers.CharField(source='student__school__name')
    student_count = serializers.IntegerField()


class FilterSerializer_caste(serializers.Serializer):
    caste = serializers.CharField(source='student__caste')
    student_count = serializers.IntegerField()
