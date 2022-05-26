from django.urls import path
from . import views

urlpatterns = [
    path('',views.Product_Add, name='product'),
    path('logout/',views.LogoutUser, name='logout'),
    path('login/',views.LoginUser, name='login'),
    path('profile/',views.Profile, name='profile'),
    path('update_profile/<int:pk>/',views.Update_Profile, name='update_profile'),
    path('update_product/<int:pk>/',views.UpdateProduct, name='update_product'),
    path('create_seller/',views.Create_User, name='create_seller'),
    path('product_details/<int:pk>/',views.ProductDetail, name='product_details'),
    ]