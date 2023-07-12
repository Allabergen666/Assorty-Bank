import base64
import logging
from io import BytesIO
from os import getenv

import qrcode
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
from requests import get

from .forms import (CategoryForm, ContactForm, PostForm, ProfileForm, UserForm, TransactionForm)
from .models import (Anime, Category, Contact, ContactSlider, HomeImage,
                     HomeRowText, Post, Profile, Transaction)
from .pars import ParsAnimeDemo

load_dotenv()
logger = logging.getLogger(__name__)


def generate_qr(request):
    try:
        if request.user.is_authenticated:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(f'http://127.0.0.1:8000/profile/{request.user.username}')
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            # fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)

            buffered = BytesIO()
            img.save(buffered, format="PNG")
            qr_image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

            context = {
                'qr_image_base64': qr_image_base64,
                'username': request.user.username,
            }

            return render(request, 'Profile/generate_qr.html', context)
        else:
            return redirect('/login')
    except Exception as e:
        logger.error('Произошла ошибка при обработке представления "generate_qr": %s', str(e))
        return redirect('/')


def index(request):
    logger.info('Обработка представления "Index"')
    try:
        obj_text = HomeRowText.objects.all()
        image_obg = HomeImage.objects.all()
        data = get(getenv("API_WEATHER").format("Almaty")).json()
        context = {
            'city': data['name'],
            'desc': data['weather'][0]['description'],
            'temp': data['main']['temp'],
            'icon': data['weather'][0]['icon'],
        }
        return render(request, "main/index.html", {"images": image_obg, "weather":context,"texts": obj_text})
    except Exception as e:
        logger.error('Произошла ошибка: %s', str(e))


def weather(request):
    logger.info('Обработка представления "Index"')
    try:
        # data = get(getenv("API_WEATHER").format("Almaty")).json()
        # context = {
        #     'city': data['name'],
        #     'desc': data['weather'][0]['description'],
        #     'temp': f"{data['main']['temp']} °C",
        #     'humidity': f"{data['main']['humidity']}%",
        #     'icon': data['weather'][0]['icon'],
        # }
        """Погода - Marselle.naz
            Страна: {data["sys"]['country']}
            Город: {data['name']} - {data['weather'][0]['description']} {data['clouds']['all']}%
            Температура: {data['main']['temp']}°C
            Ощушается: {data['main']['feels_like']}°C
            Влажность: {data['main']['humidity']}%
            Давление воздуха: {data['main']['pressure']} гПа
            Скорость ветра: {data['wind']['speed']} м/с
            Направление ветра: {data['wind']['deg']}°
            Восход солнце: {datetime.fromtimestamp(data['sys']['sunrise'])}
            Продол-ть дня: {Pr_Day}
            Закат солнце: {datetime.fromtimestamp(data['sys']['sunset'])}
        """
        data = get(getenv("API_WEATHER").format("Almaty")).json()
        context = {
            'city': data['name'],
            'desc': data['weather'][0]['description'],
            'temp': data['main']['temp'],
            'icon': data['weather'][0]['icon'],
        }
        return render(request, 'weather/weather.html', {"weather":context})
    except Exception as e:
        logger.error('Произошла ошибка: %s', str(e))


def posts(request):
    logger.info('Обработка представления "Posts"')
    try:
        Obj_All_Post = Post.objects.all()
        return render(request, "posts/post.html", {"context": Obj_All_Post})
    except Exception as e:
        logger.error('Произошла ошибка при обработке представления "Posts": %s', str(e))


def Add_Post(request):
    logger.info('Обработка представления "Add_Post"')
    try:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Добавление публикации прошло успешно!")
                return redirect("/posts")
        else:
            form = PostForm()

        return render(request, "insert/index.html", {"form": form})
    except Exception as e:
        logger.error('Произошла ошибка при обработке представления "Add_Post": %s', str(e))


def AddCategory(request):
    logger.info('Обработка представления "Добавить категорию"')
    try:
        obj_category = Category.objects.all()
        if request.method == "POST":
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Добавление категории прошло успешно!")
                return redirect("/posts")
        else:
            form = CategoryForm()
        return render(request, "insert/category.html", {"form": form, "categories": obj_category})
    except Exception as e:
        logger.error('Произошла ошибка при обработке представления "AddCategory": %s', str(e))

def logoutUser(request):
    logout(request)
    messages.success(request, 'Вы успенно вышли из учетной запики!')
    return redirect("/")


def SingUpUserView(request):
    logger.info('Обработка представления "SingUpUserView"')
    try:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                if user.password != request.POST.get('password2'):
                    messages.error(request, "Пароли не совпадают!")
                    return redirect('/singup')
                else:
                    user.set_password(user.password)
                    form.save()
                    messages.success(request, "Регистрация прошла успешно!")
                    return redirect("/")
        else:
            form = UserForm()
        return render(request, "AuthenticateUser/singup.html", {"form": form})
    except Exception as e:
        logger.error('Произошла ошибка при обработке представления "SingUpUserView": %s', str(e))


def SignInUserView(request):
    logger.info('Обработка представления "SignInUserView"')
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            if username and password:
                try:
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, 'Вы успешно вошли!')
                        return redirect("/")
                    else:
                        messages.error(request, 'Неверное имя пользователя или пароль.')
                except Exception:
                    messages.error(request, 'Произошла ошибка при аутентификации. Пожалуйста, попробуйте снова.')
            else:
                messages.error(request, 'Пожалуйста, введите имя пользователя и пароль.')

        return render(request, "AuthenticateUser/singin.html")
    except Exception as e:
        logger.error('Произошла ошибка при обработке представления "SignInUserView": %s', str(e))


def ContactView(request):
    logger.info('Обработка представления "ContactView"')
    try:
        obj_contact = Contact.objects.all()
        slider_image = ContactSlider.objects.all()
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Ваше сообщение успешно отправлено!")
                return redirect("/")
        else:
            form = ContactForm()
        return render(request, "contact/contact.html",  {"form": form, "sliders": slider_image, "contacts": obj_contact})
    except Exception as e:
        logger.error('Произошла ошибка при обработке представления "ContactView": %s', str(e))


def AnimeView(request):
    logger.info('Обработка представления "AnimeView"')
    try:
        anime_con = ParsAnimeDemo()

        for i in anime_con:
            # Проверяем, существует ли аниме с таким же заголовком
            if not Anime.objects.filter(title=i['anime_title']).exists():
                anime = Anime.objects.create(
                    image=i['anime_img'],
                    title=i['anime_title'],
                    category=", ".join(i['anime_category']),
                    description=i['anime_desc']
                )
                anime.save()

        anime_obj = Anime.objects.all().reverse()  # Используем метод reverse() для изменения порядка
        return render(request, "posts/anime.html", {"animes": anime_obj})
    except Exception as e:
        logger.error('Произошла ошибка при обработке представления "AnimeView": %s', str(e))


def UserProfileView(request):
    logger.info('Обработка представления "UserProfileView"')
    try:
        if request.user.is_authenticated:
            profile = Profile.objects.all()
            return render(request, 'Profile/profile.html', {'profile': profile})
        else:
            return redirect('/login')
    except Exception as e:
        logger.error('Произошла ошибка при обработке представления "UserProfileView": %s', str(e))
        return redirect('/')


def UserEditProfileView(request):
    logger.info('Обработка представления "UserEditProfileView"')
    try:
        if request.user.is_authenticated:
            user = request.user.profile
            if request.method == 'POST':
                new_email = request.POST.get('email')
                if new_email:
                    user_email = request.user
                    user_email.email = new_email
                    user_email.save()

                new_username = request.POST.get('username')
                if new_username:
                    user_username = request.user
                    user_username.username = new_username
                    user_username.save()
                    messages.success(request, "Редактирование username прошло успешно!")

                form = ProfileForm(request.POST, request.FILES, instance=user)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Редактирование профиля прошло успешно!")
                    return redirect('/profile')
            else:
                form = ProfileForm(instance=user)

            context = {
                'form': form,
            }

            return render(request, 'Profile/editprofile.html', context=context)
        else:
            return redirect('/login')
    except Exception as e:
        logger.error('Произошла ошибка при обработке представления "UserEditProfileView": %s', str(e))
        return redirect('/')


def TransactionView(request):
    form = TransactionForm()
    return render(request, "Transaction/transaction.html", {'form': form})