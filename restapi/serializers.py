from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import (Anime, Category, Contact, ContactSlider, HomeImage,
                         HomeRowText, Post, Profile)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class HomeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeImage
        fields = "__all__"

  
class HomeRowTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeRowText
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ContactSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSlider
        fields = "__all__"


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', "first_name", "last_name", "email", "is_staff", "is_active", "is_superuser"]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['image', 'about', 'birth_date', 'phone', 'user']
