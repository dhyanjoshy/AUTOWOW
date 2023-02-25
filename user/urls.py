from django.urls import path
from . import views



urlpatterns = [
    path('signup', views.signup,name='signup'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('dealerdetails', views.dealerdetails,name='dealerdetails'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('dash_home', views.dash_home,name='dash_home'),
    path('dash_addbrand', views.dash_addbrand,name='dash_addbrand'),

]
