from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('appointment_create/<int:num>/',  views.appointment_create, name='appointment_create'),
    path('appoitment_check/',  views.appoitment_check, name='appoitment_check'),
    path('search_appointment/',  views.search_appointment, name='search_appointment'),
    path('main_appointment/',  views.main_appointment, name='main_appointment'),
    path('generate_queue/',  views.generate_queue, name='generate_queue'),
    path('remaining_queue/',  views.remaining_queue, name='remaining_queue'),
    path('run_queue/',  views.run_queue, name='run_queue'),
    path('main_patient/',  views.main_patient, name='main_patient'),
    path('main_medicalpersonnel/',  views.main_medicalpersonnel, name='main_medicalpersonnel'),

]