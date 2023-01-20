from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('deleteCart/<str:idpd>', views.deleteCart, name='deleteCart'),
    path('service/', views.service, name='service'),
    path('signup/', views.signup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('ViewAllPd/<str:type1>',views.ViewAllPd,name='viewAllPd'),
    path('ViewPd/<str:pk>',views.ViewPd,name='viewPd'),
    path('Logout/',views.Logoutpage,name='logout'),
    path('EnterProfile/',views.EnterProfile,name='enterProfile'),
    path('ViewProfile/',views.ViewProfile,name='viewProfile'),
    path('Payment/',views.Payment,name='payment'),
]