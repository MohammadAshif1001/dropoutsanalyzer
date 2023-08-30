from rest_framework import views, response, status
from .models import School,Student,Dropout
from .serializers import SchoolSerializer, StudentSerializer, DropoutSerializer, DropoutAnalysisSerializer

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

class DropoutAnalysisView(views.APIView):
    def post(self, request):
        filter = request.data.get('filter')

        serializer = DropoutAnalysisSerializer(data={'filter': filter})
        if serializer.is_valid():
            instance = serializer.create(serializer.validated)

