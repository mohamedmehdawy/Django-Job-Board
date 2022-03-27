from django.urls import path
from . import views
app_name = "accounts"
urlpatterns = [
    path('signup/', views.SignUp, name="sing_up"),
    path('profile/', views.profile, name="profile"),
    path('profile_edit', views.profile_edit, name="profile_edit")
]