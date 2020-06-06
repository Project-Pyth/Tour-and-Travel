from django.contrib import admin

from myapp.models import PersonalProfile
from myapp.models import Profilee
from myapp.models import TourPost
from myapp.models import packages_tour,About
from myapp.models import Delhi,Chandigarh,Rajasthan,Himachal
from myapp.models import Cab
from myapp.models import UProfile
from myapp.models import Book,checkout,gallery


admin.site.register(PersonalProfile)
admin.site.register(Profilee)
admin.site.register(TourPost)
admin.site.register(packages_tour)
admin.site.register(About)
admin.site.register(Delhi)
admin.site.register(Chandigarh)
admin.site.register(Rajasthan)
admin.site.register(Himachal)
admin.site.register(Cab)
admin.site.register(UProfile)
admin.site.register(Book)
admin.site.register(checkout)
admin.site.register(gallery)


