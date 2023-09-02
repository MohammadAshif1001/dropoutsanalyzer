from rest_framework import views, response, status,mixins,generics
from .models import School,Student,Dropout
from .serializers import SchoolSerializer, StudentSerializer, DropoutSerializer,FilterSerializer_state,FilterSerializer_school,FilterSerializer_city,FilterSerializer_caste
from django.db.models import Count

class SchoolView(views.APIView):
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class StudentView(views.APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

class DropoutView(views.APIView):
    def get(self, request):
        dropouts = Dropout.objects.all()
        serializer = DropoutSerializer(dropouts, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

class FilterStudents_state(mixins.ListModelMixin,generics.GenericAPIView):
    serializer_class=FilterSerializer_state
    queryset=Dropout.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        distinct_states = Dropout.objects.values('student__school__state').distinct()
        for state in distinct_states:
            queryset = Dropout.objects.values('student__school__state').annotate(student_count=Count('student__school__state')).order_by('student__school__state')     

        return queryset

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    



class FilterStudents_city(mixins.ListModelMixin,generics.GenericAPIView):
    serializer_class=FilterSerializer_city
    queryset=Dropout.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()

        distinct_city = Dropout.objects.values('student__school__city').distinct()
        for city in distinct_city:
            queryset = Dropout.objects.values('student__school__city').annotate(student_count=Count('student__school__city')).order_by('student__school__city')       

        return queryset

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    



class FilterStudents_school(mixins.ListModelMixin,generics.GenericAPIView):
    serializer_class=FilterSerializer_school
    queryset=Dropout.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        distinct_states = Dropout.objects.values('student__school__name').distinct()
        for state in distinct_states:
            queryset = Dropout.objects.values('student__school__name').annotate(student_count=Count('student__school__name'))        

        return queryset

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    

class FilterStudents_caste(mixins.ListModelMixin,generics.GenericAPIView):
    serializer_class=FilterSerializer_caste
    queryset=Dropout.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        distinct_states = Dropout.objects.values('student__caste').distinct()
        for state in distinct_states:
            queryset = Dropout.objects.values('student__caste').annotate(student_count=Count('student__caste'))        

        return queryset

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)