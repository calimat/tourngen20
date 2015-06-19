from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import render
# Create your views here.
def home_page(request):
    return render(request, 'home.html', {
        'new_tournament_name': request.POST.get('tournament_name', ''),
    })