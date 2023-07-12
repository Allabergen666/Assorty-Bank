from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import (Anime, Category, Contact, ContactSlider, HomeImage,
                     HomeRowText, Post, Profile)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'phone', 'get_image')
    list_filter = ('birth_date',)
    search_fields = ('user__username', 'user__email')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150px" />')
        return 'Not image'
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at',
                    'location', 'description', 'get_image']
    list_filter = ['category', 'created_at', 'location']
    search_fields = ['title']

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="200px"')
        return 'Not Image'


@admin.register(HomeImage)
class HomeImageAdmin(admin.ModelAdmin):
    list_display = ["created_at", "get_image"]
    list_filter = ["created_at"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="200px"')
        return 'Not Image'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "created_at"]
    list_filter = ["email", "created_at"]
    search_fields = ["name", "email"]


@admin.register(ContactSlider)
class ContactSliderAdmin(admin.ModelAdmin):
    list_display = ["created_at", "get_image"]
    list_filter = ["created_at"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="200px"')
        return 'Not Image'


@admin.register(HomeRowText)
class HomeRowTextAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title"]


@admin.register(Anime)
class AnimeForm(admin.ModelAdmin):
    list_display = ["title", "category", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title"]