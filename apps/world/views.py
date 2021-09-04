from django.shortcuts import render

# Create your views here.
def leaflet_test(request):
    return render(request, 'leaflet-test.html')