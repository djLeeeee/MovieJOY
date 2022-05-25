from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.my_profile),
    path('profile/<username>/', views.profile),
    path('profile_image/<int:profile_number>/', views.profile_image_update),
    path('sms_auth/', views.is_auth),
    path('sms_auth/<phone_number>/', views.sms_send),
    path('sms_auth/<phone_number>/<int:auth_number>/', views.sms_auth),
]
