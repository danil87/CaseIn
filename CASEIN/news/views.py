from django.shortcuts import render
from .models import Activity
from django.views.generic import DetailView


def news_home(request):
    news = Activity.objects.order_by('-date')
    return render(request, 'news/news_home.html' , {'news': news})


class NewDetailView(DetailView):
    model = Activity
    template_name = 'news/details_view.html'
    context_object_name = 'activity'



