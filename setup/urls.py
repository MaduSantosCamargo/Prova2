
from django.contrib import admin
from django.urls import path
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('producao/', home_views.producao),
    path('engenharia/', home_views.engenharia),
    path('controle_qualidade/', home_views.controle_qualidade),
    path('expedicao/', home_views.expedicao),
]
