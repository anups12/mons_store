from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.Home, name='home'),
    path('signin/',views.Create_Customer, name='signin'),
    path('logincust/',views.CustomerLogin, name='logincust'),
    path('logoutcust/',views.CustomerLogout, name='logoutcust'),
    path('profilecust/',views.ProfileCustomer, name='profilecust'),
    path('update_cust_profile/',views.Update_Profile_customer, name='update_cust_profile'),
    path('shop/<str:mc>/<str:sc>/<str:br>/',views.Shop, name='shop'),
    path('wishlist/',views.Wishlistprod, name='wishlist'),
    path('wishlist/<str:pk>/',views.Wishlistprod, name='wishlist'),
    path('deletewishlist/<str:pk>/',views.DeleteWishlist, name='deletewishlist'),
    path('cart/',views.Cart, name='cart'),
    path('prod_detail/<int:pk>',views.ProductDetail, name='prod_detail'),
    path('update_cart/',views.Update_cart, name='update_cart'),
    path('checkout/',views.Checkout, name='checkout'),
    path('payment/',views.PaymentPage, name='payment'),
    path('contact/',views.ContactUs, name='contact'),


# <------------------Reset password views------------------------>
    path('reset_password/',auth_view.PasswordResetView.as_view(template_name='customer/password_reset.html'), name='reset_password'),
    path('reset_password_sent/',auth_view.PasswordResetDoneView.as_view(template_name='customer/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='customer/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/',auth_view.PasswordResetCompleteView.as_view(template_name='customer/password_reset_done.html'), name='password_reset_complete'),


    ]