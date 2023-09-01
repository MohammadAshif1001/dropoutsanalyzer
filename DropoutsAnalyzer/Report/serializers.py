from rest_framework import serializers
from .models import School, Student, Dropout


class SchoolSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = School
        fields = ['name', 'city', 'state']

class StudentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Student
        fields = ['name', 'gender', 'caste', 'age', 'standard']


class DropoutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dropout
        fields = '__all__'


class FilterSerializer(serializers.Serializer):
    state = serializers.CharField(source='student__school__state')
    student_count = serializers.IntegerField()

    # def state(self):
    #     return self.student__school__state