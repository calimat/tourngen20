from django.shortcuts import render, redirect
from django.http import HttpResponse
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
    form = TeamForm()
    if request.method == 'POST':
        form = TeamForm(data=request.POST)
        if form.is_valid():
            form.save(tournament=tournament)
            return redirect(tournament)
    return render(request, 'tournament.html', {'tournament': tournament, "form": form})


def new_tournament(request):
    form = TeamForm(data=request.POST)
    if form.is_valid():
        tournament = Tournament.objects.create()
        form.save(tournament=tournament)
        return redirect(tournament)
    else:
        return render(request, 'home.html', {"form": form})

