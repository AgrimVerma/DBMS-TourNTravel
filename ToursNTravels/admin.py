from django.contrib import admin

# Register your models here.
from ToursNTravels.models import *

admin.site.register(user)
admin.site.register(booking)
admin.site.register(train)
admin.site.register(flight)
admin.site.register(location)
admin.site.register(attraction)
admin.site.register(purchase)
admin.site.register(hotel)
admin.site.register(review)
admin.site.register(payment)
# admin.site.register(user)
