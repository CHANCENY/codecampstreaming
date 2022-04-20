from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.indexpage, name='landing-page'),
    path('homepage',views.homecomingpage, name='home-page'),
    path('login',views.loginingpage, name='login-page'),
    path('register',views.registrationpage, name='registration-page'),
    path('streaming',views.coursevideostowatching, name='watching-page'),
    path('accounting',views.accountpersonal, name='Account-page'),
    path('logout',views.logout, name='logout-page'),
    path('checkcourses',views.campcoderooms, name='course-page'),
    path('loginfirst',views.loginfirstuser, name='first-login-page'),
    path('login/homepage',views.homecomingpage, name='home-page'),
    path('coursepagelayout',views.layoutpage, name='layout-page'),
    path('lookout',views.functionsearchingvideos, name='searching-page'),
    path('changepassword',views.changepage, name='change-page'),
    path('forgotpassword',views.verifyingchange, name='verify-page'),
    path('passmessage',views.feedback, name='feedback-page'),
    path('mailreciever',views.receivingmailofrequest, name='email-page'),

    path('reset_password/',auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    ]