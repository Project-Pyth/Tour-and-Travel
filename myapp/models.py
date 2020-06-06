from datetime import date

from django.db import models
from django.contrib.auth.models import User,auth
from django.db.models import Model
from django.db.models.signals import post_save
from django.dispatch import receiver





class PersonalProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=100 , default="")
    city = models.CharField(max_length=100, default="")
    Phone = models.BigIntegerField()
    website = models.URLField(default="")
    image = models.ImageField(upload_to='profile_image/', blank=True)

    def __str__(self):
       return self.user.username

   # @receiver(post_save, sender=User)
   #def create_user_profile(sender,instance,created,**kwargs):
        #if created:
            #UserProfile.objects.create(user = instance)
            #instance.Userprofile.save()



#class Booking(models.Model):
    #country = models.CharField(max_length=128)
    #departure_date = models.DateField()
    #return_date = models.DateField()
    #first_name = models.CharField(max_length=100)
    #last_name = models.CharField(max_length=100)
    #vehicle_type = models.CharField(max_length=100)
    #number_of_adults = models.IntegerField()
    #number_of_children = models.IntegerField()
    #email = models.EmailField(default="")
    #phone = models.IntegerField(default="")


class Profilee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profilee.objects.create(user=instance)
        instance.profilee.save()


class TourPost(models.Model):
    package_id = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    description = models.CharField(max_length=1000)
    cost = models.IntegerField()
    Image = models. ImageField(upload_to='tour_pics',null=True)


class packages_tour(models.Model):
    package_id = models.AutoField
    place_name = models.CharField(max_length=50)
    category = models.CharField(max_length= 50,default ="")
    subcategory = models.CharField(max_length=50)
    cost = models.IntegerField()
    desc = models. CharField(max_length=600)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='package_pics')

    def __str__ (self):
        return self.place_name


#class detail(models.Model):
   # pid = models.ForeignKey(packages_tour,on_delete=models.PROTECT)
   # planame = models.CharField(max_length=225)
   # pcost = models.IntegerField()
   # pcategory = models.CharField(max_length=255)
  #  pdesc = models.CharField(max_length=225)


class About(models.Model):
   msg_id = models.AutoField(primary_key = True)
   name = models.CharField(max_length=100)
   eid = models.CharField(max_length = 225)
   city = models.CharField(max_length = 100)
   subject = models.CharField(max_length = 500)

   def __str__(self):
        return self.name


class Delhi(models.Model):


    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.source


class Chandigarh(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.source



class Rajasthan(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.source



class Himachal(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.source



class Cab(models.Model):
    cabid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    phone = models.BigIntegerField()
    pick = models.DateField()
    drop = models.DateField()


class UProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics',null=True,default='default.jpg')
    dob = models.DateTimeField(null=True)
    bio = models.CharField(max_length=225)
    city = models.CharField(max_length=225)

class Book(models.Model):
    bid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200,default="")
    depart_date = models.DateField()
    arrive_date = models.DateField()
    city = models.CharField(max_length=100,default="")
    state = models.CharField(max_length=100,default="")

class checkout(models.Model):
    bid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    depart_date = models.DateField()
    arrive_date = models.DateField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class gallery(models.Model):
    title = models.CharField(max_length=100)
    descrip = models.CharField(max_length=1000)
    imge = models.ImageField(upload_to='gallery_images')
    pub = models.DateField()

    def __str__(self):
        return self.title

