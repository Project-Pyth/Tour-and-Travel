
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User,auth

from django.contrib.auth import login

# Create your views here.
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View




from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm

from django1_project import settings
from . import checksum

from .models import UProfile, Book, checkout
from myapp.models import packages_tour,About,Cab,gallery

from myapp.models import TourPost,Delhi,Chandigarh,Rajasthan,Himachal
from myapp.tokens import account_activation_token

from django.core.mail import EmailMessage
from math import ceil


MERCHANT_KEY = "c9a#ZpJZcq%T3AO_"



def hello(request):
    text = "<h1> hi,welcome to site</h1>"
    return HttpResponse(text)


def index(request):
    return render(request, "myapp/index.html")


def home(request):

    return render(request, "myapp/home.html")


def thanks(request):
    return render(request, "myapp/thanks.html")



def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pass1 = request.POST['password']

        user = auth.authenticate(username=un, password=pass1)
        if user is not None:
            auth.login(request, user)
            request.session['username'] = un
            request.session['id'] = user.id
            request.session.set_expiry(300)
            messages.success(request, " You are successfully logged in")

            return render(request, 'myapp/home.html',{"data": un, "Flag": True})
        else:
            messages.error(request, 'Invalid credentials')
            return render(request,'myapp/login.html',{"status":"Invalid credentials"})
    else:
        return render(request, 'myapp/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/home')


def register(request):
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']
        un = request.POST['uname']
        pass1 = request.POST['pass']
        pass2 = request.POST['pass2']

        if pass1 == pass2:

            if User.objects.filter(username=un).exists():
                messages.error(request, 'This Username was already Taken')
                # print("Username Taken")
                return redirect('/register')

            if not un.isalnum():
                messages.error(request,"Username should contain only letters and numbers")
                return redirect('/register')

            if len(un) > 12:
                messages.error(request,"Username must be under 12 characters")
                return redirect('/register')


            elif User.objects.filter(email=em).exists():
                messages.info(request, "This Email was Already Taken")
                # print("Username Taken")
                return redirect('/register')
            else:
                user = User.objects.create_user(username=un, email=em, password=pass1, first_name=fn, last_name=ln)
                user.is_active = False
                user.save()

                # print('user created !')


                #current_site = get_current_site(request)


                #message = render_to_string('myapp/acc_activate_email.html',
                   # {
                   # 'user': user,

                   # 'domain': current_site.domain,
                   # 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                   # 'token': account_activation_token.make_token(user),
                   # })

                #mail_subject = 'Activate Your Tour and travel Account'
                #to_em = request.POST['email']
               # email = EmailMessage(mail_subject,message,to=[to_em])
                #email.send()
                #user.email_user(subject, message)
                # send_mail(
                #     "Hello User",
                #     "Welcome to Email Confirmation",
                #     "corejavabtes@gmail.com",
                #     [em],
                #     fail_silently=False,
                # )
                #send_mail(
                    #subject,
                    #message,
                    #'btespython1101@gmail.com',
                    #[em],
                    #fail_silently=False,
                   #)

                messages.info(request, ('Please confirm your email address to complete the registration '))
                return redirect('/login')

                # return render(request,'index.html')

        else:
            print('password not matched !')
            messages.info(request, 'register')

        return redirect('/register')



    else:
        return render(request, "myapp/register.html")





def view_gallery(request):
    gal = gallery.objects.all()
    context = {'gal':gal}
    return render(request, "myapp/gallery.html",context)

#profile
def view_profile(request):
    return render(request,'myapp/profile.html')

def seeprofile(request):
     profile = UProfile.objects.all()
     context = {'profile':profile}

     return render(request,'myapp/showp.html',context)

def dev_info(request):
    return render(request,'myapp/dev_info.html')




def about(request):
    return render(request, "myapp/about.html")

def video(request):
    return render(request, "myapp/video.html")




def checkout(request):
    if request.method == "POST":
        name = request.POST.get('pname','')
        address = request.POST.get('address','')
        depart_date = request.POST.get('depart_date','')
        arrive_date = request.POST.get('arrive_date','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        demo = Book(name=name, address=address, depart_date=depart_date, arrive_date=arrive_date, city=city, state=state)
        if len(name) < 3:
            messages.error(request, " name should not be less than 3 characters.")
            return redirect('/checkout')
        demo.save()
        return redirect('/process_payment')
    else:
        context = {}
        idd = request.GET["checkid"]
        obj = packages_tour.objects.get(id=idd)
        context["packages"] = obj
        return render(request, "myapp/checkout.html",context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('uname','')
        eid = request.POST.get('email','')
        city = request.POST.get('city','')
        subject = request.POST.get('subject','')
        obj = About(name=name, eid=eid, city=city, subject=subject)
        obj.save()
    return render(request, "myapp/contact.html")

#blog
def blog(request):
    allPosts = TourPost.objects.all()
    context = {'allPosts':allPosts}
    return render(request, "myapp/blog.html",context)


def blogpost(request):
    context = {}
    id = request.GET["bid"]
    obj = TourPost.objects.get(id=id)
    context["post"] = obj

    return render(request, "myapp/blogpost.html",context)

#cab booking
def delhi(request):
    obj = Delhi.objects.all()

    return render(request,"myapp/delhi.html",{'obj':obj})


def chandigarh(request):
    chd = Chandigarh.objects.all()
    context = {'chd':chd}

    return render(request,"myapp/chandigarh.html",context)


def rajasthan(request):
    raj = Rajasthan.objects.all()
    context = {'raj':raj}

    return render(request,"myapp/rajasthan.html",context)



def himachal(request):
    him = Himachal.objects.all()
    context = {'him':him}

    return render(request,"myapp/himachal.html",context)



def cab(request):
    if request.method == "POST":
        name = request.POST['name']
        mail = request.POST['mail']
        phone = request.POST['mobile']
        pick = request.POST['pick']
        drop = request.POST['drop']
        obj = Cab(name=name, mail=mail, phone=phone, pick=pick, drop=drop)
        if len(phone) < 10 :
            messages.error(request,"Phone no. should not be less than 10 digits.")
            return redirect('/cab')
        elif len(name)<3:
            messages.error(request, "username should not less than 2 characters.")
            return redirect('/cab')


        obj.save()
        return redirect('/process_payment')
    else:
        return render(request, "myapp/cab.html")



def booking(request):
    return render(request,"myapp/booking.html")

# package
@login_required()
def package(request):
    #packages = packages_tour.objects.all()
    #print(packages)
    #n = len(packages)
    #nslides = n // 4 + ceil((n / 4) - (n // 4))
        allpacks = []
        catpacks = packages_tour.objects.values('category','id')
        cats = {item['category'] for item in catpacks}
        for cat in cats:
            pack = packages_tour.objects.filter(category=cat)
            n = len(pack)
            nslides = n // 4 + ceil((n / 4) - (n // 4))
            allpacks.append([pack,range(1, nslides),nslides])
        #params = {'no_of_slides':nslides , 'range':range(1,nslides) , 'packages_tour':packages}
        #allpacks = [[packages,range(1,nslides),nslides],
                    #[packages,range(1,nslides),nslides]]
        params = {'allpacks':allpacks}
        return render(request,"myapp/package.html",params)


def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.place_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allpacks = []
    catpacks = packages_tour.objects.values('category', 'id')
    cats = {item['category'] for item in catpacks}
    for cat in cats:
        packtemp = packages_tour.objects.filter(category=cat)
        pack = [item for item in packtemp if searchMatch(query, item)]
        n = len(pack)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        if len(pack)!= 0:
            allpacks.append([pack, range(1, nslides), nslides])
    params = {'allpacks': allpacks,"msg":""}
    if len(allpacks) ==0 or len(query)<4:
        params = {'msg':"Please Make sure  to enter relevant search query"}
    return render(request, "myapp/search.html", params)



def package_detail(request):
    context ={}
    id = request.GET["pid"]
    obj = packages_tour.objects.get(id=id)
    context["packages"] = obj
    return render(request,"myapp/package_detail.html",context)


def allpackages(request):
    allpacks = packages_tour.objects.all()
    params = {'allpacks': allpacks}
    return render(request,"myapp/allpackages.html",params)

class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            #uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
           user.is_active = True
           user.save()
           return render(request,'myapp/home.html',{"data":user.first_name,"Flag":True})
        else:
            messages.warning(request, ('The confirmation link was invalid!'))
            return redirect('/thanks')


def demo(request):

    return render(request,"myapp/demo.html")


def readmore(request):
    context = {}
    idd1 = request.GET["gid"]
    obj = gallery.objects.get(id=idd1)
    context["gallery"] = obj
    return render(request,"myapp/readmore.html",context)


def paymentMode(request):
    param_dict = {
        "MID": "MOxQFd68674997735960",
        "ORDER_ID":"765",
        "CUST_ID": "20",
        "TXN_AMOUNT": "2",
        "CHANNEL_ID": "WEB",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "WEBSTAGING",
        #"CALLBACK_URL": "http/127.0.0.1:8000/handleRequest/",
        "CALLBACK_URL":"https://merchant.com/callback/"

    }
    param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict,MERCHANT_KEY)

    return render(request,'myapp/paytm.html',{'params':param_dict})

@csrf_exempt
def handlerequest(request):
    #paytm will send you post request here
    return redirect(request,'myapp/thanks.html')


def process_payment(request):

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'item_name': "packages_tour.object.filter(place_name)",
        'invoice': "1",
        'amount' : "111",
        'notify_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('paypal-ipn')),
        #'return_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           #reverse('payment-done')),
        #'cancel_rerturn': 'http://{}{}'.format("127.0.0.1:8000",
                                          # reverse('payment-cancelled')),
    }
    if "Book_id" in request.session:
        book_id = request.session["book_id"]
        book_obj = get_object_or_404(Book,id=book_id)
        book_obj.save()

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'myapp/process_payment.html', { 'form': form})

@csrf_exempt
def payment_done(request):
    return render(request,"myapp/done.html")

def payment_cancelled(request):
    return HttpResponse(" Your payment is cancelled")




