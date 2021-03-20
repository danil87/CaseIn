from django.urls import path
from . import views
urlpatterns = [
    path('', views.news_home),
    path('<int:pk>', views.NewDetailView.as_view(), name='news-detail')
]
