from django.contrib import admin
from django.urls import path

from TO_DO import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
   path('register',views.register,name="register"),
   path('login',views.logining,name="login"),
   path('logout',views.logouting,name="logout"),
   path('',views.show_mission_list,name="mission_list"),
   path('mission_detail/<int:pk>',views.show_mission_detail,name="mission_detail"),
   path('mission_update/<int:pk>',views.mission_update,name="mission_update"),
   path('mission_delete/<int:pk>',views.mission_delete,name="mission_delete"),
   path('add_mission',views.add_mission,name="add_mission"),
]
