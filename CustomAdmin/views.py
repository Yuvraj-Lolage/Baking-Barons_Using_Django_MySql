from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.models import User
from BakersApp.models import Cakes, Feedback, TutorialVideo
from django.contrib import messages
from .forms import AddCakeForm, AddTutorialForm #forms.py
from .functions import handle_uploaded_file #functions.py
# Create your views here.

def render_loginPage(request):
    return render(request, 'adminLogin.html')

def renderDashboard(request):
    return render(request, 'dashboard.html')
    
def loginSuperAdmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']        
        user = authenticate(username = username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                messages.success(request, "Log in as Administrator Successfull.")
                return redirect('dashboard')
        messages.error(request, "Log in as Administrator Unsuccessfull. You are not Super Admin")    
    return redirect('/admin/')

def logoutSuperAdmin(request):
    logout(request)
    return redirect('/admin/')

def renderUserPage(request):
    allUsers = User.objects.all()
    return render(request, 'users.html', { 'users':allUsers })

def renderCakePage(request):
    allCakes = Cakes.objects.all()
    cake = AddCakeForm()
    return render(request, 'cakes.html', { 'cakes': allCakes,
                                           'form': cake,})

def renderFeedbackPage(request):
    allFeedbacks = Feedback.objects.all()
    return render(request, 'feedbacks.html', { 'feedbacks': allFeedbacks})

def renderTutorialPage(request):
    allTutorialVideos = TutorialVideo.objects.all()
    tutorial = AddTutorialForm()
    return render(request, 'tutorialVideo.html', { 'tutorials': allTutorialVideos,
                                                  'form' : tutorial})


def deleteUser(request, id):
    user = User.objects.get(id = id)
    user.delete()
    messages.success(request, 'User Deleted!')
    return redirect('/admin/users')
 
def deleteCake(request, id):
    cake = Cakes.objects.get(id = id)
    cake.delete()
    messages.success(request, 'Cake Deleted!')
    return redirect('/admin/cakes')

def deleteTutorial(request, id):
    tutorial = TutorialVideo.objects.get(id = id)
    tutorial.delete()
    messages.success(request, 'Tutorial Video Deleted!')
    return redirect('/admin/tutorialVideo')

def addCake(request):
    if request.method == 'POST':
        student = AddCakeForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['Cake_Image'])
            model_instance = student.save(commit=False)
            model_instance.save()
            messages.success(request, 'Cake Added!')
            return redirect('/admin/cakes')
    else:
        student = AddCakeForm()
        messages.error(request, 'Cake Not Added!')
        return render(request, 'cakes.html', { 'form': student})

def editCake(request, id):
    cakeObj = Cakes.objects.get(id = id)
    
    if request.method == 'POST':
        cakeName = request.POST['cakeName']
        cakeFlavour = request.POST['cakeFlavour']
        cakePrice = request.POST['cakePrice']
        cakeReview = request.POST['cakeReview']
        cakeCategory = request.POST['cakeCategory']
        
        handle_uploaded_file(request.FILES['Image'])
        cakeObj.Cake_Name = cakeName
        cakeObj.Cake_Flavour = cakeFlavour
        cakeObj.Cake_Price = cakePrice
        cakeObj.Cake_Review = cakeReview
        cakeObj.category = cakeCategory 
        cakeObj.Cake_Image = request.FILES['Image']
    try:
        cakeObj.save()
        messages.success(request, "Changes Successful")
    except Exception as e:
        messages.error(request, "Error in ")
    return redirect('/admin/cakes')


def editUser(request, id):
    userObj = User.objects.get(id = id)
    isSuperUser = request.POST['isSuperUser']
    isActiveUser = request.POST['isActiveUser']
    
    if isSuperUser == 'True':
        userObj.is_superuser = 1
    else:
        userObj.is_superuser = 0
            
    if isActiveUser == 'True':
        userObj.is_active = 1
    else:
        userObj.is_active = 0
    
    try:
        userObj.save()    
        messages.success(request,"User is Modified!")
    except Exception as e:
        messages.error(request,"User is not Modified!")
    return redirect('/admin/users') 


def addTutorialVideo(request):
    tutorialForm = AddTutorialForm(request.POST, request.FILES)
    if tutorialForm.is_valid():
        handle_uploaded_file(request.FILES['Video_File'])
        handle_uploaded_file(request.FILES['Video_Thumbnail'])
        model_instance = tutorialForm.save(commit=False)
        model_instance.save()
        messages.success(request, 'Tutorial Video Added!')
        return redirect('/admin/tutorialVideo')
    else:
        tutorialForm = AddTutorialForm()
        messages.error(request, 'Cake Not Added!')
        return render(request, 'tutorialVideo.html', { 'form': tutorialForm})


def editTutorialVideo(request, id):
    tutorialObj = TutorialVideo.objects.get(id = id)
    if request.method == "POST":
        videoTitle = request.POST['title']
        videoDesc = request.POST['description']
        videoFile = request.FILES['videoFile']
        thumbnailFile = request.FILES['thumbnaiImage']
        
        tutorialObj.Video_Title = videoTitle
        tutorialObj.Video_description = videoDesc
        tutorialObj.Video_File = videoFile
        tutorialObj.Video_Thumbnail = thumbnailFile
        
    try:
        tutorialObj.save()    
        messages.success(request,"Tutorial Video is Modified!")
    except Exception as e:
        messages.error(request,"Tutorial Video is not Modified!")
    return redirect('/admin/tutorialVideo')