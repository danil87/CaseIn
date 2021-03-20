from django.urls import path
from . import views
urlpatterns = [
        path('', views.index),
        path('begin', views.begin, name='begin'),
        path('endreg', views.endreg, name='endreg'),
        path('search', views.Search.as_view(), name='search'),
        path('sotrud', views.search_home),
        path('panel-sotrud', views.panel),
        path('search_new', views.search_new),
        path('<int:pk>', views.PanelViews.as_view(), name='panels'),
        path('bezops', views.bezopas),
        path('nav', views.glav),
        path('history', views.history),
        path('karier', views.karier),
        path('tech', views.tech),
        path('karier_btn', views.karier_btn),
        path('karier_ekonom', views.karier_ekonom),
        path('karier_yadr', views.karier_yadr),
        path('register', views.register),
        path('userlogin', views.userlogin),
        path('logout', views.userlogout),
        path('<int:pk>/update', views.SotrudUpdateView.as_view(), name='sotrud-update'),
        path('lklk', views.bd, name='lk')
]