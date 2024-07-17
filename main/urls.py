from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='cats'),
    path('info', views.info, name='dogs'),
    path('family', views.family, name='fam'),
    path('felidae', views.felidae, name='felidae'),
    path('canidae', views.canidae, name='canidae')
] 