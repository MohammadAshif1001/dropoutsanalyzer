from django.shortcuts import render
from django.views import View
import requests

class HomePage(View):
    template_name='home.html'
    def get(self,request):
        api_url = 'http://127.0.0.1:8000/filter/state'  # Replace with the actual API URL

        try:
            response = requests.get(api_url)

            if response.status_code == 200:
                json_data = response.json()
            else:
                json_data = {'error': 'Failed to fetch data'}

        except requests.exceptions.RequestException as e:
            json_data = {'error': f'Request error: {e}'}

        context = {
            'api_data': json_data['results'],  # Add the API data to the context
        }
        return render(request,self.template_name,context)
