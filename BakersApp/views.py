from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from typing import Protocol
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token


from .models import BirthdayCakes, AnniversaryCakes, ThemeCakes, Cart, Cakes, TutorialVideo, Feedback
# Create your views here.
def renderHomepage(request):
    feedbackObject = Feedback.objects.all()
    cnt = 0
    for x in feedbackObject:
        cnt += 1
    return render(request, 'Home.html',{"feedback":feedbackObject,
                                        "feedbackCount":cnt})


def renderSignup(request):
    return render(request, 'singup.html')

#updated function:
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can Proceed with your account.")
        return redirect('renderLogin')
    else:
        messages.error(request, "Activation link is invalid!")
        
    return redirect('/')


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear {user}, please go to you email {to_email} inbox and click on \
                received activation link to confirm and complete the registration.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')


def signupUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        myUser = User.objects.create_user(username, email, password)
        myUser.first_name = firstname
        myUser.last_name = lastname
        #updated
        myUser.is_active=False
        myUser.save()
        activateEmail(request, myUser, email)
    return redirect('/')

def renderLogin(request):
    return render(request, 'Login.html')


def loginUser(request):
    if request.method == 'POST':
        global email
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        # print(email, username, password)
        user = authenticate(username = username, password=password)
        if user is not None:
            login(request,user)
    return redirect("/")

        
        
def logoutUser(request):
    logout(request);
    return redirect('/')



#function for Render Birthday cake Menu
def renderBirhdayMenu(request):
    # birthdayCakeObject = BirthdayCakes.objects.all()
    birthdayCakeObject = Cakes.objects.filter(category = 1)
    return render(request, 'BirthdaycakeMenu.html', { "birthdayCake":birthdayCakeObject })


#function for Render Anneversary cake Menu
def renderAnniversaryMenu(request):
    # anniversaryCakeObject = AnniversaryCakes.objects.all()
    anniversaryCakeObject = Cakes.objects.filter(category = 2)
    return render(request, 'AnniversarycakeMenu.html', {"anniversaryCake":anniversaryCakeObject})


#function for Render Theme cake Menu
def renderThemeMenu(request):
    # themeCakeObject = ThemeCakes.objects.all()
    themeCakeObject = Cakes.objects.filter(category = 3)
    return render(request, 'ThemecakeMenu.html', {"themeCake":themeCakeObject})

# function for render custom cake page
def renderCustomCakeForm(request):
    return render(request, 'Customize_Cake.html')


# function for render cookie page
def renderCookieMenu(request):
    cookieObject = Cakes.objects.filter(category = 4)
    return render(request, 'CookieMenu.html', {'cookieMenu':cookieObject})

#function for render quickorder page
def quickOrderCake(request, id):
    cake_name = Cakes.objects.get(id=id).Cake_Name
    birthdayCake = Cakes.objects.filter(Cake_Name__iexact=cake_name)
    return render(request, 'cakeDesc.html', { "birthdaycake" : birthdayCake })

@login_required
def addToCart(request):
    if request.method == 'POST':
        cakeName = request.POST.get('name')
        cakePrice = int(request.POST.get('price'))
        cakeQuantity = request.POST.get('qty')
        total = (int(cakePrice)*int(cakeQuantity));
        cakeSize = request.POST.get('size')
        
        cakeImg = Cakes.objects.get(Cake_Name = cakeName).Cake_Image
        cakeId = Cakes.objects.get(Cake_Name = cakeName).id
        cakeFlavour = Cakes.objects.get(Cake_Name = cakeName).Cake_Flavour
        cartObj = Cart()
        cartObj.CakeId = cakeId
        cartObj.userId = request.user.id
        cartObj.username = request.user
        cartObj.Cake_Name = cakeName
        cartObj.Cake_Quantity = cakeQuantity
        cartObj.CakePrice = cakePrice
        cartObj.Cake_Size = cakeSize
        cartObj.TotalPrice = total
        cartObj.Cake_Image = cakeImg
        cartObj.Cake_flavour = cakeFlavour
        cartObj.save()

    return render(request, 'Home.html')


# function for render cart for particlar user
@login_required
def renderCart(request):
    bill = 0
    cnt = 0
    cartObj = Cart.objects.filter(userId=(request.user).id)    
    for x in cartObj:
        bill+=int(x.TotalPrice)
        cnt += 1
    return render(request, 'cart.html', {'cart':cartObj,
                                         'bill':bill,
                                         'items':cnt})
# function for edit cart
def editCart(request, id):
    cart_item = Cart.objects.get(CakeId = id, userId = (request.user.id))
    cart_item.delete()
    return redirect('renderCart')


# function for render payment gateway
def renderPaymentGateway(request):
    return render(request, 'paymentGatewatway.html')


#function for rendering Myorder
def renderMyOrders(request):
    return render(request, 'myorder.html')

#function to render aboutus Page
def renderAboutus(request):
    return render(request, 'AboutUs.html')

def renderDecoratingTutorial(request):
    tutVidObj = TutorialVideo.objects.all()
    return render(request, 'Tutorial.html', {'video':tutVidObj})

def saveFeedback(request):
    if request.method == 'POST':
        email = (request.user).email
        quality = request.POST.get('text')
        description = request.POST.get('feedback')
        starRating = request.POST.get('star')
        
        FeedbckObj = Feedback()
        FeedbckObj.Feedback_Email = email
        FeedbckObj.Feedback_Quality = quality
        FeedbckObj.Feedback_Description = description
        FeedbckObj.Feedback_StarRating = starRating
        FeedbckObj.save()
        
       
    return redirect("/")





