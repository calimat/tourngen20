from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import render
# Create your views here.
def home_page(request):
   # if request.method == 'POST':
      #  return HttpResponse(request.POST['id_tournament_name'])
    return render(request, 'home.html')