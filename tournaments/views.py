from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.shortcuts import render
from tournaments.models import Team, Tournament
# Create your views here.
from django.core.exceptions import ValidationError

def home_page(request):
    return render(request, 'home.html')

def view_tournament(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    if request.method == 'POST':
        Team.objects.create(name=request.POST['team_name'], tournament=tournament)
        return redirect('/tournaments/%d/' % (tournament.id,))
    return render(request, 'tournament.html', {'tournament': tournament})

def new_tournament(request):
   tournament = Tournament.objects.create()
   team = Team.objects.create(name=request.POST['team_name'], tournament=tournament)
   try:
       team.full_clean()
       team.save()
   except ValidationError:
       tournament.delete()
       error = "Please enter a name for your team"
       return render(request, 'home.html', {"error": error})
   return redirect('/tournaments/%d/' % (tournament.id,))

