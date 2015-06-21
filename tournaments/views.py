from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.shortcuts import render
from tournaments.models import Team, Tournament
# Create your views here.

def home_page(request):
    return render(request, 'home.html')

def view_tournament(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    return render(request, 'tournament.html', {'tournament': tournament})

def new_tournament(request):
   tournament = Tournament.objects.create()
   Team.objects.create(name=request.POST['team_name'], tournament=tournament)
   return redirect('/tournaments/%d/' % (tournament.id,))

def add_team(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    Team.objects.create(name=request.POST['team_name'], tournament=tournament)
    return redirect('/tournaments/%d/' % (tournament.id,))