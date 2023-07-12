from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=125, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True,
         verbose_name="Дата создания")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Post(models.Model):
    image = models.ImageField(upload_to="posts/",
        verbose_name="Изображение")
    title = models.CharField(max_length=125,
        verbose_name="Заголовок")
    description = models.TextField(max_length=500,
        verbose_name="Описание")
    category = models.ForeignKey(Category, 
        on_delete=models.CASCADE, 
        verbose_name="Категория")
    location = models.CharField(max_length=125,
        verbose_name="Место проведения")
    created_at = models.DateTimeField(auto_now_add=True,
         verbose_name="Дата создания")
    
    def __str__(self):
        return f"{self.title} - {self.category} - {self.created_at}"
    
    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"


class HomeImage(models.Model):
    image = models.ImageField(upload_to="home_image", 
        verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True,
         verbose_name="Дата создания")
    
    def __str__(self) -> str:
        return f"Изображение созданная в {self.created_at}"
    
    class Meta:
        verbose_name = "Изображения Главной Странницы"


class HomeRowText(models.Model):
    title = models.CharField(max_length=125, verbose_name="Заголовок")
    description = models.TextField(max_length=500, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True,
         verbose_name="Дата создания")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Row Text Главное Странницы"
        verbose_name_plural = "Row Text Главных Странниц"


class Contact(models.Model):
    name = models.CharField(max_length=125,
        verbose_name="Имя")
    email = models.EmailField(max_length=125,
        verbose_name="Почта")
    message = models.TextField(max_length=500,
        verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True,
         verbose_name="Дата создания")
    
    def __str__(self):
        return f"{self.name} - {self.created_at}"
    
    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class ContactSlider(models.Model):
    image = models.ImageField(upload_to="contact_slider", 
        verbose_name="Изображение", help_text="Размер изображения - 3840x2160")
    created_at = models.DateTimeField(auto_now_add=True,
         verbose_name="Дата создания")
    
    def __str__(self):
        return f"Изображение созданная в - {self.created_at}"
    
    class Meta:
        verbose_name = "Сладер Контакта"
        verbose_name_plural = "Сладеры Контактов"


class Anime(models.Model):
    image = models.URLField(verbose_name="Ссылка на изображение")
    title = models.CharField(max_length=125, verbose_name="Название")
    category = models.CharField(max_length=125, verbose_name="Категория")
    description = models.TextField(max_length=800, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.title} - {self.category} - {self.created_at}"
    
    class Meta:
        verbose_name = "Аниме"
        verbose_name_plural = "Аниме"


class Profile(models.Model):
    image = models.ImageField(upload_to="profile/", 
        verbose_name="Фотография", help_text="Картинка должна быть Х на Х",
        blank=True, null=True)
    
    balance = models.PositiveBigIntegerField(default=0, verbose_name="Баланс")

    phone = models.CharField(max_length=20, unique=True, verbose_name="Номер телефона",
        blank=True, null=True)
    
    birth_date = models.DateField(verbose_name="Дата рождения",
        blank=True, null=True)
    
    about = models.TextField(max_length=200,
        verbose_name="Обо мне", blank=True, null=True)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
        verbose_name="Пользователь")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user.first_name.title()} {self.user.first_name.title()[0]}."

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ["-created_at"]


class Transaction(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name="sent_transaction", verbose_name="Sender")
    recipient = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name="recipient_transaction", verbose_name="Resipient")
    summa = models.PositiveBigIntegerField(default=100, verbose_name="Summ")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.sender.balance < self.summa:
            raise Exception("недостаточно средств на балансе")
        
        self.sender.balance -= self.summa
        self.recipient.balance += self.summa
        self.sender.save()
        self.recipient.save()
        # super лбращатся к родительскому классу и сохрани значени, родител это клас в котором он есть 
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.sender_id} -> {self.recipient_id}"
    
    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        ordering = ["-created_at"]