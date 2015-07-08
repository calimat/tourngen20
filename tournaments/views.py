from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.shortcuts import render
from tournaments.models import Team, Tournament
# Create your views here.
from django.core.exceptions import ValidationError
from tournaments.forms import TeamForm
from tournaments.models import Team, Tournament

def home_page(request):
    return render(request, 'home.html', {'form': TeamForm()})

def view_tournament(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    error = None

    if request.method == 'POST':
        try:
           team = Team.objects.create(name=request.POST['name'], tournament=tournament)
           team.full_clean()
           team.save()
           return redirect(tournament)
        except ValidationError:
            error = "Please enter a name for your team"
    return render(request, 'tournament.html', {'tournament': tournament, 'error': error})



def new_tournament(request):
   tournament = Tournament.objects.create()
   team = Team.objects.create(name=request.POST['name'], tournament=tournament)
   try:
       team.full_clean()
       team.save()
   except ValidationError:
       tournament.delete()
       error = "Please enter a name for your team"
       return render(request, 'home.html', {"error": error})
   return redirect(tournament)

