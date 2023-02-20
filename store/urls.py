from django.urls import path
from . import views



urlpatterns = [
    path('', views.home,name='home'),
    path('brand/<brand>', views.brand,name='brand'),
    path('products/<brand_id>', views.products,name='products'),
    path('single_product/<product_id>', views.single_product,name='single_product'),
    path('loan_calculator', views.loan_calculator,name='loan_calculator'),
]
