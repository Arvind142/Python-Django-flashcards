from django.urls import path
from . import views
urlpatterns = [
    #path('',),
    path('',views.home,name="home"),
    path('Addition.html',views.Addition,name="Addition"),
    path('Subraction.html',views.Subraction,name="Subraction"),
    path('Multiplication.html',views.Multiplication,name="Multiplication"),
    path('Division.html',views.Division,name="Division"),
    
]