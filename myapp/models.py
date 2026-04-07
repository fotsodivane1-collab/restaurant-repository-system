from django.db import models
from django.utils.translation import gettext_lazy as _

class Restaurant(models.Model):
    name = models.CharField(max_length = 200)
    cuisine_type = models.CharField(max_length = 200)
    address = models.CharField(max_length = 300)
    is_halal = models.BooleanField(default = False)
    hero_image = models.ImageField(upload_to = 'restaurant/images/')
    language_code = models.CharField(max_length = 10, default = 'EN')
    total_reviews = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.name


class Page(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    PAGE_CHOICES = [
        ('home', 'Home'),
        ('reserve', 'Reserve'),
        ('order', 'Order'),
        ('gallery', 'Gallery'),
        ('reviews', 'Reviews'),
        ('menu', 'Menu'),
        ('contact', 'Contact'),
    ]
    page_name = models.CharField(max_length = 200, choices = PAGE_CHOICES)
    slug = models.SlugField(max_length=200, unique=True)
    url = models.CharField(max_length = 300, blank = True)
    display_order = models.IntegerField(default = 0)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.page_name


    def get_absolute_url(self):
        return f"/{self.slug}/"


class OpeningHours(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    day = models.CharField(max_length=20, choices = DAY_CHOICES)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f"{self.day}: {self.opening_time} - {self.closing_time}"


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=200)
    rating = models.FloatField()
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name} - {self.rating}/5"


class ActionButton(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    BUTTON_CHOICES = [
        ('reserve', _('Reserve')),
        ('order', _('Order')),
        ('login', _('Login')),        
        ('register', _('Register')),  
    ]

    ICON_CHOICES = [
        ('calendar', 'Calendar'),   
        ('globe', 'Globe'),                  
        ('user', 'User'),           
        ('user_plus', 'UserPlus'),  
    ]
    label = models.CharField(max_length=  200)
    button_type = models.CharField(max_length=20, choices = BUTTON_CHOICES)
    icon_type = models.CharField(max_length = 20, choices=ICON_CHOICES, 
                                  default='globe')
    icon = models.ImageField(upload_to=  'buttons/icons/', 
                              blank = True, null = True)
    url = models.URLField(max_length = 300, blank = True)
    url_name = models.CharField(max_length = 200, blank = True)
    display_order = models.IntegerField(default = 0) 
    is_active = models.BooleanField(default = True)
    requires_auth = models.BooleanField(default = False)
    guests_only = models.BooleanField(default = False)

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return self.url if self.url else f"/{self.url_name}/"
    
class RestaurantLocation(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    street_address = models.CharField(max_length =300)
    city = models.CharField(max_length = 100)
    postal_code = models.CharField(max_length = 20)
    country = models.CharField(max_length = 100)
    latitude = models.DecimalField(max_digits = 9, decimal_places=6)
    longitude = models.DecimalField(max_digits = 9, decimal_places=6)
    icon = models.ImageField(upload_to = 'location/icons/', 
                              blank=True, null=True)

    def __str__(self):
        return f"{self.street_address}, {self.postal_code} {self.city}"


    def get_google_maps_url(self):
        return f"https://www.google.com/maps?q={self.latitude},{self.longitude}"

    def get_full_address(self):
        return f"{self.street_address}, {self.postal_code} {self.city}, {self.country}"
    


