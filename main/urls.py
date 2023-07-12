from django.urls import path

from .views import (Add_Post, AddCategory, AnimeView, ContactView,
                    SignInUserView, SingUpUserView, UserEditProfileView,
                    UserProfileView, index, logoutUser, posts, generate_qr, weather, TransactionView)

urlpatterns = [
    path('', index),
    path('anime/', AnimeView),
    path("posts/", posts),
    path("add/", Add_Post),
    path("category/", AddCategory),
    path("singup/", SingUpUserView),
    path("logout/", logoutUser),
    path("login/", SignInUserView),
    path("contact/", ContactView),
    path('profile/', UserProfileView),
    path('profile/edit/', UserEditProfileView),
    path('qr/', generate_qr),
    path('weather/almaty/', weather),
    path('profile/transaction', TransactionView),
]
