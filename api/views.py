import requests
from django.http import JsonResponse
from django.views import View

class HelloView(View):
    def get(self, request):
        visitor_name = request.GET.get('visitor_name', 'Guest')
        client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')

        #fetching the city
        try:
            response=requests.get(f"//ipinfo.io/{client_ip}/json")
            location_data = response.json()

            city = location_data.get('city', 'Unknown')
        except Exception as e:
            city = "unknown"
            print(f"error fetching location data: {e}")

        response = {
            "client_ip": client_ip,
            "location": city,
            "greeting": f"Hello, {visitor_name}!, the temperator is 11 degrees celcius in new york"
        }
        return JsonResponse(response)

# Create your views here.
