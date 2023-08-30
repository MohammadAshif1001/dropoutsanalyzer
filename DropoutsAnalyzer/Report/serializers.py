from rest_framework import serializers
from .models import School, Student, Dropout


class SchoolSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = School
        fields = ['name', 'area']

class StudentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Student
        fields = ['name', 'gender', 'caste', 'age', 'standard']


class DropoutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dropout
        fields = ['reason', 'date']

    student = StudentSerializer()

class DropoutAnalysisSerializer(serializers.Serializer):
    filter = serializers.CharField()
    data = serializers.ListField()

    def create_data(self, filter):
        data = []

        if filter == 'school wise':
            schools = School.objects.all()

            for school in schools:
                dropout_count = Dropout.objects.filter(student__school=school).count()

                data.append({'school': school.name, 'dropout_count': dropout_count})

        elif filter == 'area wise':
            areas = School.objects.values_list('area', flat=True).distinct()

            for area in areas:
                dropout_count = Dropout.objects.filter(student__school__area=area).count()

                data.append({'area': area, 'dropout_count': dropout_count})

        elif filter == 'gender wise':
            genders = Student.objects.values_list('gender', flat=True).distinct()

            for gender in genders:
                dropout_count = Dropout.objects.filter(student__gender=gender).count()

                data.append({'gender': gender, 'dropout_count': dropout_count})

        elif filter == 'caste wise':
            castes = Student.objects.values_list('caste', flat=True).distinct()

            for caste in castes:
                dropout_count = Dropout.objects.filter(student__caste=caste).count()

                data.append({'caste': caste, 'dropout_count': dropout_count})

        elif filter == 'age/standard wise':
            ages_and_standards = Student.objects.values_list('age', 'standard').distinct()

            for age, standard in ages_and_standards:
                dropout_count = Dropout.objects.filter(student__age=age, student__standard=standard).count()

                data.append({'age': age, 'standard': standard, 'dropout_count': dropout_count})

        return data

    def validate_filter(self, value):
        valid_filters = ['school wise', 'area wise', 'gender wise', 'caste wise', 'age/standard wise']

        if value not in valid_filters:
            raise serializers.ValidationError('Invalid filter. Please choose one of these: {}'.format(', '.join(valid_filters)))

        return value

    def create(self, validated_data):
        filter = validated_data.get('filter')

        data = self.create_data(filter)

        return DropoutAnalysisSerializer(filter=filter, data=data)

