from rest_framework import views, response, status,mixins,generics
from .models import School,Student,Dropout
from .serializers import SchoolSerializer, StudentSerializer, DropoutSerializer,FilterSerializer
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

class FilterStudentsMixin(mixins.ListModelMixin,generics.GenericAPIView):
    serializer_class=FilterSerializer
    queryset=Dropout.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        state = self.request.query_params.get('state')
        

        # if state:
        distinct_states = Dropout.objects.values('student__school__state').distinct()
        for state in distinct_states:
            queryset = Dropout.objects.values('student__school__state').annotate(student_count=Count('student__school__state'))        

        return queryset

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)