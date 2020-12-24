from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/info/', views.profile_page_view, name='user_profile'),
    path('profile/signup_user/', views.signup_user_view, name="signup_user"),
    path('profile/signup_doctor/', views.signup_doctor_view, name="signup_doctor"),
    path('profile/logout/', views.logout_view, name='logout'),
    path('profile/login/', views.login_view, name='login'),
    path('profile/main/', views.profile_page_view, name='user_profile_main'),
    path('profile/recomend/', views.profile_page_view, name='user_profile_recomend'),
    path('profile/grafik/', views.profile_page_view, name='user_profile_grafik'),
    path('profile/consalt/', views.profile_page_view, name='user_profile_consalt'),
    path('profile/settings/', views.profile_page_view, name='user_profile_settings'),
    path('profile/videos/', views.profile_page_view, name='user_profile_videos'),
    path('profile/articles/', views.profile_page_view, name='user_profile_articles'),
    path('save_main_data', views.save_main_data, name='save_main_data'),
    path('save_doctor_data', views.save_doctor_data, name='save_doctor_data'),
    path('change_user_pass', views.change_user_pass, name='change_user_pass'),
    path('save_support_message', views.save_support_message, name='save_support_message'),
    path('save_user_doc', views.save_user_doc, name='save_user_doc'),
    path('remove_user_doc/', views.remove_user_doc, name='remove_user_doc'),
    path('save_data_success/', views.save_data_success, name='save_data_success'),
    path('save_verification_success/', views.save_verification_success, name='save_verification_success'),
    path('send_file_for_verified/', views.send_file_for_verified, name='send_file_for_verified'),
    path('profile/pass_reset/', authViews.PasswordResetView.as_view(template_name='profile/password_reset.html', email_template_name='profile/password_reset_email.html'), name="pass_reset"),
    path('profile/password_reset_complete/', authViews.PasswordResetCompleteView.as_view(template_name='profile/password_reset_complete.html'), name="password_reset_complete"),
    path('profile/password_reset_confirm/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name='profile/password_reset_confirm.html'), name="password_reset_confirm"),
    path('profile/password_reset_done/', authViews.PasswordResetDoneView.as_view(template_name='profile/password_reset_done.html'), name="password_reset_done"),
]