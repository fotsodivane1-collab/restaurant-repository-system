from django.views.generic import RedirectView
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    # Reserve page  ← ADD THIS LINE
    path('reserve/', views.reserve, name='reserve'),
    # Order page
    path('order/', views.order, name='order'),
    # Gallery page
    path('gallery/', views.gallery, name='gallery'),
    # Reviews page
    path('reviews/', views.reviews, name='reviews'),
    # Menu page
    path('menu/', views.menu, name='menu'),
    # Contact page
    path('contact/', views.contact, name='contact'),
    # Login and Register
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    # Location
    path('location/', views.location, name='location'),
    # Redirect old waitlist URL
    path('waitlist/', RedirectView.as_view(url='/reserve/'), name='waitlist'),
    # Dynamic pages - MUST be last
    path('<slug:slug>/', views.page_detail, name='page_detail'),
]