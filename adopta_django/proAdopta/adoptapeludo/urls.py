from django.contrib import admin
from django.urls import path
from .views import index,perros,gatos,contacto,ubicacion,gracias,gracias2,loki,princesa,timmy,adoptar,bigotes,manchita,sara

urlpatterns = [
    path('',index,name='IND'),
    path('perros/',perros,name='PER'),
    path('gatos/',gatos,name='GAT'),
    path('contacto/',contacto,name='CON'),
    path('ubicacion/',ubicacion,name='UBI'),
    path('gracias/',gracias,name='GRA'),
    path('gracias/',gracias2,name='GRC'),
    path('loki/',loki,name='LOK'),
    path('princesa/',princesa,name='PRI'),
    path('timmy/',timmy,name='TIM'),
    path('adoptar/',adoptar,name='ADO'),
    path('bigotes/',bigotes,name='BIG'),
    path('manchita/',manchita,name='MAN'),
    path('sara/',sara,name='SAR'),
]
