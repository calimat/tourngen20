from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.shortcuts import render
from tournaments.models import Team
# Create your views here.

def home_page(request):
    return render(request, 'home.html')

def view_tournament(request):
    teams = Team.objects.all()
    return render(request, 'tournament.html', {'teams': teams})

def new_tournament(request):
   Team.objects.create(name=request.POST['team_name'])
   return redirect('/tournaments/the-only-tournament-in-the-world/')