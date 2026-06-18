from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('login/',views.user_login,name='login'),
    path('signin/',views.sign_in,name='signin'),
    path('logout/',views.logout_view,name='logout'),
    path('add_product/', views.add_product, name='add_product'),
    path('update/<int:id>/', views.update_product, name='update_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
]