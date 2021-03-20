from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm, UserLoginForm, MembersForm
from .models import Members
from django.views.generic import DetailView
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView,ListView, UpdateView
from django.db import connection
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin




def index(request):
    return render(request, 'main/index.html')

def begin(request):
    if request.user.is_authenticated:
        std = Members.objects.all()
        return render(request, 'main/begin.html', {'std': std})
    else:
        return render(request, 'main/begin.html')


def endreg(request):
    if not request.user.is_authenticated:
        cur = connection.cursor()
        cur.execute('UPDATE main_members SET zp = 35000 WHERE dolznost = \'Экономист\';')
        cur = connection.cursor()
        cur.execute('UPDATE main_members SET zp = 45000 WHERE dolznost = \'Программист\';')
        cur = connection.cursor()
        cur.execute('UPDATE main_members SET zp = 40000 WHERE dolznost = \'Ядерщик\';')

        return render(request, 'main/endreg.html')#, data)


def search_home(request):
    if request.user.is_staff:
        search = Members.objects.all()
        return render(request, 'main/search_results.html', {'search_list': search})


def search_new(request):
    return render(request, 'main/search_new.html')



class Search(ListView):
    def get_queryset(self):
        return Members.objects.filter(name__icontains = self.request.GET.get("q"))


def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context["q"] = self.request.GET.get("q")
    return context


def panel(request):
    if request.user.is_staff:
        return render(request, 'main/panel.html')


class PanelViews(DetailView):
    model = Members
    template_name = 'main/panel.html'
    context_object_name = 'panel'


def view(request):
    if request.method == 'POST':
        nmid = request.POST['nmid']


def bezopas(request):
    if request.user.is_authenticated:
        return render(request, 'main/bezopas.html')

def glav(request):
    if request.user.is_authenticated:
        return render(request, 'main/glav.html')

def history(request):
    if request.user.is_authenticated:
        return render(request, 'main/history.html')


def karier(request):
    if request.user.is_authenticated:
        return render(request, 'main/karier.html')

def tech(request):
    if request.user.is_authenticated:
        return render(request, 'main/Tech.html')

def karier_btn(request):
    if request.user.is_authenticated:
        return render(request, 'main/karier_btn.html')

def karier_ekonom(request):
    if request.user.is_authenticated:
        return render(request, 'main/karier_ekonom.html')

def karier_yadr(request):
    if request.user.is_authenticated:
        return render(request, 'main/karier_yadr.html')

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('endreg')
        else:
            form = UserRegisterForm()
        return render(request, 'main/register.html', {"form": form})



def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserLoginForm(data = request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return render(request, 'main/index.html')
        else:
            form = UserLoginForm()
        return render(request, 'main/login.html', {"form": form})

def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'main/index.html')

class SotrudUpdateView(LoginRequiredMixin, UpdateView):
    model = Members
    template_name = 'main/update.html'
    form_class = MembersForm
    raise_exception = True


def bd(request):
    if request.user.is_authenticated:
        std=Members.objects.all()
        return render(request, 'main/lklk.html', {'std': std})
