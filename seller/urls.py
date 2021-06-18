from django.urls import path,re_path
from django.views.generic import TemplateView

from seller import views

urlpatterns = [
    path('str_c/',TemplateView.as_view(template_name='Seller Templates/store.html'),name='crt_str'),
    path('buyer_seller/', TemplateView.as_view(template_name="Seller Templates/login_register.html"),
         name="buyer_seller"),
    path('find_str/',TemplateView.as_view(template_name='Seller Templates/single_store.html'),name='get_store'),

    path('store/',views.find_store,name='single_store'),

    path('otp/', views.sendotp, name='otp'),
    path('checkuser/',views.check_user,name='checkotp'),
    path('cust_ac/',views.c_account,name='c_ac'),

    path('crt_str/',views.store,name='crt_store'),
    path('my_str/',views.my_stores,name='my_str'),
    path('logout/',views.logout,name='logout'),

]
