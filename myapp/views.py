from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Restaurant, Page, Review, ActionButton, RestaurantLocation


def home(request):
    restaurant = Restaurant.objects.first()
    pages = Page.objects.filter(
        is_active = True).order_by('display_order')
    buttons = ActionButton.objects.filter(
        is_active = True).order_by('display_order')
    reviews = Review.objects.filter(
        restaurant = restaurant).order_by('-date_added')
    location = RestaurantLocation.objects.filter(
        restaurant = restaurant).first()

    context = {
        'restaurant': restaurant,
        'pages': pages,
        'buttons': buttons,
        'reviews': reviews,
        'location': location,
    }
    return render(request, 'myapp/home.html', context)


def page_detail(request, slug):
    """Dynamic page by slug"""
    page = get_object_or_404(Page, slug=slug)
    context = {'page': page}
    return render(request, 'myapp/page_detail.html', context)


def reserve(request):
    return render(request, 'reserve/reserve.html')


def order(request):
    return render(request, 'myapp/order.html')


def gallery(request):
    return render(request, 'myapp/gallery.html')


def reviews(request):
    restaurant = Restaurant.objects.first()
    reviews = Review.objects.filter(
        restaurant=restaurant).order_by('-date_added')
    context = {'reviews': reviews}
    return render(request, 'myapp/reviews.html', context)


def menu(request):
    return render(request, 'myapp/menu.html')


def contact(request):
    location = RestaurantLocation.objects.first()
    context = {'location': location}
    return render(request, 'myapp/contact.html', context)


def location(request):
    """Redirect to Google Maps"""
    location = RestaurantLocation.objects.first()
    if location:
        return redirect(location.get_google_maps_url())
    return redirect('myapp:home')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('myapp:home')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('myapp:home')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('myapp:home')


from django.utils.translation import gettext as _

def home(request):
    context = {
        'welcome':       _('Welcome to our restaurant'),
        'open_status':   _('Open today until 01:00'),
        'book_now':      _('Book Now'),
        'order_now':     _('Order Now'),
        'reserve':  _('reserve'),
        'login':         _('Login'),
        'reviews':       _('Reviews'),
    }
    return render(request, 'myapp/home.html', context)
