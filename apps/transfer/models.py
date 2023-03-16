from django.db import models

#my imports
from apps.users.models import User

# Create your models here.
class HistoryTransfer(models.Model):
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="from_user",
        verbose_name="от пользователя"
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="to_user",
        verbose_name="пользователю"
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время"
    )
    amount = models.CharField(
        max_length=255,
        verbose_name="Количество"
    )
    
    def __str__(self):
        return self.amount 
    
    class Meta:
        verbose_name = "История"
        verbose_name_plural = "История"