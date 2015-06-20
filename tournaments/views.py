from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.shortcuts import render
from tournaments.models import Team
# Create your views here.
# def home_page(request):
#     if request.method == 'POST':
#         Team.objects.create(name=request.POST['team_name'])
#         return redirect('/')
#     teams = Team.objects.all()
#     saved_team = teams[0]
#     return render(request, 'home.html', {'new_team': saved_team})

# def home_page(request):
#     if request.method == 'POST':
#         new_item_text = request.POST['team_name']  #1
#         Team.objects.create(name=new_item_text)  #2
#     else:
#         new_item_text = ''  #3
#
#     return render(request, 'home.html', {
#         'new_item_text': new_item_text,  #4
#     })

# def home_page(request):
#     if request.method == 'POST':
#         Team.objects.create(name=request.POST['team_name'])
#         return redirect('/')
#
#     return render(request, 'home.html')

def home_page(request):
    if request.method == 'POST':
        Team.objects.create(name=request.POST['team_name'])
        return redirect('/')

    teams = Team.objects.all()
    return render(request, 'home.html', {'teams': teams})