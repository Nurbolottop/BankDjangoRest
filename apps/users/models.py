from django.db import models
from django.contrib.auth.models import AbstractUser
import secrets

class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name="Почта",
        blank = True, null = True,
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name="Телефонный номер",
        blank = True, null = True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    age = models.PositiveIntegerField(
        verbose_name="Возраст",
        blank = True, null = True,
    )
    balance = models.CharField(
        max_length=255,
        verbose_name="Баланс",
        blank = True, null = True,
        default=0
    )
    wallet_address = models.CharField(
        max_length=12,
        verbose_name="Кошелек",
        blank = True, null = True,
        unique=True
    )
    def __str__(self):
        return self.wallet_address 
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        
    def save(self, *args, **kwargs):
        if not self.wallet_address:
            self.wallet_address = secrets.token_hex(6)
        super().save(*args, **kwargs)
        
