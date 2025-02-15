from . import views 
from django.urls import path 

urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout',views.logout, name='accounts.logout'),
    path('orders/', views.orders, name='accounts.orders'),
]