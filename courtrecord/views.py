from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import loader

from .models import Evidence, Source, Battle
from .forms import EvidenceForm, CreateUserForm, BattleForm


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'accounts/register.html', context)

@login_required(login_url='login')
def homePage(request):
    evidence = Evidence.objects.all()
    battles = Battle.objects.all()
    context = {'evidence':evidence, 'battles':battles}
    return render(request, 'home.html', context)

@login_required(login_url='login')
def create_evidence(request):
    if request.method == 'POST':
        form = EvidenceForm(request.POST, request.FILES)
        if form.is_valid():
            #icon = request.FILES['icon']
            evidence = form.save(commit=False)
            evidence.legalUser = request.user
            evidence.save()
            return redirect('home')  # Redirect to home after saving
        else:
            return render(request, 'newEvidence.html', {'form': form})
    else:
        form = EvidenceForm()
        return render(request, 'newEvidence.html', {'form': form})

@login_required(login_url='login')
def delete(request, id):
  todelete = Evidence.objects.get(id=id)
  todelete.delete()
  return redirect('home')

@login_required(login_url='login')
def update(request, id):
  tochange = Evidence.objects.get(id=id)
  context = { 'tochange': tochange, }
  return render(request, 'update.html',context)

@login_required(login_url='login')
def updaterecord(request, id):
    title = request.POST['title']
    description = request.POST['description']
    category = request.POST['category']
    legalUser = request.user
    tochange = Evidence.objects.get(id=id)
    tochange.title = title
    tochange.description = description
    tochange.category = category
    tochange.legalUser = legalUser
    tochange.save()
    return redirect('home')  # Redirect to home after saving

@login_required(login_url='login')
def create_battle(request):
    if request.method == 'POST':
        form = BattleForm(request.POST)
        if form.is_valid():
            battle = form.save(commit=False)
            battle.save()
            battle.legalUser.add(request.user)
            battle.save()
            return redirect('home')  # Redirect to home after saving
        else:
            return render(request, 'newBattle.html', {'form': form})
    else:
        form = BattleForm()
        return render(request, 'newBattle.html', {'form': form})

@login_required(login_url='login')
def deletebattle(request, id):
  todelete = Battle.objects.get(id=id)
  todelete.delete()
  return redirect('home')

@login_required(login_url='login')
def updatebattle(request, id):
  tochange = Battle.objects.get(id=id)
  context = { 'tochange': tochange, }
  return render(request, 'updatebattle.html',context)

@login_required(login_url='login')
def updatebattlerecord(request, id):
    year = request.POST['year']
    verdict = request.POST['verdict']
    legalUser = request.user
    tochange = Battle.objects.get(id=id)
    tochange.year = year
    tochange.verdict = verdict
    tochange.legalUser.add(request.user)
    tochange.save()
    return redirect('home')  # Redirect to home after saving