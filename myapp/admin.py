from django.contrib import admin

from myapp.models import Restaurant
admin.site.register(Restaurant)
from myapp.models import Page
admin.site.register(Page)
from myapp.models import OpeningHours
admin.site.register(OpeningHours)
from myapp.models import Review
admin.site.register(Review)
from myapp.models import ActionButton
admin.site.register(ActionButton)
from myapp.models import RestaurantLocation
admin.site.register(RestaurantLocation)