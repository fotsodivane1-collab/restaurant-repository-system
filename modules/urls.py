#users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/',  views.login_view,  name='login'),
    path('logout/', views.logout_view, name='logout'),
]

#revenue
urlpatterns = [
    path('',            views.order_list,   name='order_list'),
    path('new/',        views.order_create, name='order_create'),
    path('<int:pk>/',   views.order_detail, name='order_detail'),
]

#product
urlpatterns = [
    path('',                            views.dish_catalog,       name='dish_catalog'),
    path('<int:pk>/',                   views.dish_detail,        name='dish_detail'),
    path('<int:pk>/surge/',             views.apply_surge_pricing,name='apply_surge_pricing'),
]