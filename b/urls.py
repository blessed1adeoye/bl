from django.urls import path
from . import views




app_name = 'b'

urlpatterns = [

    path('', views.one, name='home'),
    path('about-me/', views.two, name='about'),
    path('Contact', views.contact, name='cont'),
    path('pandemic', views.RESEARCH, name='res'),
    path('pandemic/<int:pk>/', views.Proj, name='pandemic'),
    path('WEEKLY_HEALTH_INFORMATION/', views.dx, name='weekly'),
    path('WEEKLY_HEALTH_INFORMATION/<int:pk>/', views.wkDx, name='him'),


    
]