from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_loginPage,),
    path('loginSuperAdmin', views.loginSuperAdmin, name='loginSuperAdmin'),
    path('dashboard', views.renderDashboard, name='dashboard'),
    path('logout', views.logoutSuperAdmin, name='logout'),
    path('users', views.renderUserPage, name='users'),
    path('cakes', views.renderCakePage, name='cakes'),
    path('feedbacks', views.renderFeedbackPage, name='feedbacks'),
    path('tutorialVideo', views.renderTutorialPage, name='tutorialVideo'),
    path('deleteUser/<int:id>', views.deleteUser, name='deleteUser'),
    path('deleteCake/<int:id>', views.deleteCake, name='deleteCake'),
    path('deleteTutorial/<int:id>', views.deleteTutorial, name='deleteTutorial'),
    path('addCake', views.addCake, name='addCake'),
    path('editCake/<int:id>', views.editCake, name='editCake'),
    path('editUser/<int:id>', views.editUser, name='editUser'),
    
    
]