from django.shortcuts import render
from django.views import View
from Report.models import Student,School,Dropout
import requests
from datetime import date



class HomePage(View):
    template_name='home.html'
    def get(self,request):
        return render(request,self.template_name)



class Charts_api():
    def request_data(self,url):
        api_url = url  

        try:
            response = requests.get(api_url)

            if response.status_code == 200:
                return response.json()
            else:
                return {'error': 'Failed to fetch data'}

        except requests.exceptions.RequestException as e:
            return {'error': f'Request error: {e}'}



class ChartPage(View):
    template_name='charts.html'
    def get(self,request):
        api=Charts_api()
        states_data=api.request_data(request.build_absolute_uri('/filter/state'))
        castes_data=api.request_data(request.build_absolute_uri('/filter/caste'))
        cities_data=api.request_data(request.build_absolute_uri('/filter/city'))
        
        total_students=Student.objects.count()
        total_schools=School.objects.count()

        start_date = date(2023, 1, 1)
        end_date = date(2023, 12, 31)
        total_dropouts=Dropout.objects.filter(date__range=(start_date, end_date)).count()
        context = {
            'states_data': states_data['results'],
            'castes_data': castes_data['results'],
            'cities_data': cities_data['results'],
            'total_students':total_students,
            'total_schools':total_schools,
            'total_dropouts':total_dropouts
        }
        return render(request,self.template_name,context)


class VolunteerPage(View):
    template_name='volunteer.html'
    def get(self,request):
        instance=Student.objects.all().order_by('age').values()
        context={
        'students':instance
        }
        return render(request,self.template_name,context)
