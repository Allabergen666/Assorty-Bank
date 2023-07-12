from django.contrib.auth.models import User
from django.forms import (DateInput, EmailInput, FileInput, ModelForm,
                          PasswordInput, Select, Textarea, TextInput, NumberInput)
from .models import Category, Contact, Post, Profile, Transaction


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Категория",
            }),
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["image", "title", "description", "category", "location"]
        widgets = {
            "image": FileInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control form-control-dark",
                "type": "file",
                "placeholder": "Изображение",
                }),
            "title": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control form-control-dark",
                "type": "text",
                "placeholder": "Заголовок",
            }),
            "description": Textarea(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control form-control-dark",
                "type": "text",
                "placeholder": "Описание",
                "cols": "30",
                "rows": "10",
            }),
            'category': Select(attrs={
                "style": "margin: 20px; width: 1190px;",
                'class': 'form-control form-control-dark'
            }),
            "location": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control form-control-dark",
                "type": "text",
                "placeholder": "Заголовок",
            }),
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        widgets = {
            "first_name": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "First name",
            }),
            "last_name": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Last name",
            }),
            "username": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Username",
            }),
            "email": EmailInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "E-mail",
            }),
            "password": PasswordInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Password",
            }),
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
        widgets = {
            "name": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Name",
            }), 
            "email": EmailInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "E-mail",
            }),
            "message": Textarea(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Message",
                "cols": "30",
                "rows": "10",
            }),
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'about', 'birth_date', 'phone']
        widgets = {
            'image': FileInput(attrs={
                'style': 'width: 145px; margin: 40px;',
                'class': 'form-control text-bg-dark',
                'placeholder': 'Изображение',
            }),
            'about': Textarea(attrs={
                'style': 'border: none;',
                "rows": "6",
                'class': 'form-control text-bg-dark',
                'placeholder': 'О себе!',
            }),
            'birth_date': DateInput(attrs={
                'style': 'border: none;',
                'class': 'form-control text-bg-dark',
                'min': '1900-01-01',
                'placeholder': 'Дата рождения',
            }),
            'phone': TextInput(attrs={
                'style': 'border: none;',
                'class': 'form-control text-bg-dark',
                'placeholder': 'Номер телефона',
            })
        }


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['sender', 'recipient', 'summa']
        widgets = {
            'sender':Select(attrs={

            }),
            'recipient':Select(attrs={

            }),
            'summa':NumberInput(attrs={
                
            })
        }