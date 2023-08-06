from django.urls import path
from . import views

urlpatterns = [
    path('', views.renderHomepage, name='renderHomepage'),
    path('renderSignup', views.renderSignup, name='renderSignup'),
    path('signupUser', views.signupUser, name='signupUser'),
    path('renderLogin', views.renderLogin, name='renderLogin'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('logout', views.logoutUser, name='logout'),
    path('renderBirthdayMenu', views.renderBirhdayMenu, name="renderBirthdayMenu"),
    path('renderAnneversaryMenu', views.renderAnniversaryMenu, name='renderAnneversaryMenu'),
    path('renderThemeMenu', views.renderThemeMenu, name='renderThemeMenu'),
    path('<int:id>', views.quickOrderCake, name='quickOrder'),
    path('addToCart', views.addToCart, name='addToCart'),
    path('renderCart', views.renderCart, name='renderCart'),
    path('renderCustomCakeForm', views.renderCustomCakeForm, name='renderCustomCakeForm'),
    path('renderCart/<int:id>', views.editCart, name='editcart'),
    path('renderPaymentGateway', views.renderPaymentGateway, name='renderPaymentGateway'),
    path('renderCookieMenu', views.renderCookieMenu, name="renderCookieMenu"),
    path('renderMyOrders', views.renderMyOrders, name='renderMyOrders'),
    path('renderAboutus', views.renderAboutus, name='renderAboutus'),
    path('renderDecoratingTutorial', views.renderDecoratingTutorial, name='renderDecoratingTutorial'),
    path('saveFeedback', views.saveFeedback, name='saveFeedback'),
    
    
]