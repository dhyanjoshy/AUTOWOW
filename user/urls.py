from django.urls import path
from . import views



app_name='user'



urlpatterns = [
    path('signup', views.signup,name='signup'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('dealerdetails', views.dealerdetails,name='dealerdetails'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('dash_home', views.dash_home,name='dash_home'),
    path('dash_addbrand', views.dash_addbrand,name='dash_addbrand'),
    path('dash_addproduct', views.dash_addproduct,name='dash_addproduct'),
    path('dash_urproduct', views.dash_urproduct,name='dash_urproduct'),
    path('dash_single_product/<product_id>', views.dash_single_product,name='dash_single_product'),
    path('dash_addcolor/<product_id>', views.dash_addcolor,name='dash_addcolor'),
    path('dash_addvarient/<product_id>', views.dash_addvarient,name='dash_addvarient'),
    path('dash_enquiries', views.dash_enquiries,name='dash_enquiries'),

]
