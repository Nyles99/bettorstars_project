from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Tournaments(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название турнира',
        help_text='Введите название для вашего турнира'
    )
    ticket_price = models.IntegerField(blank=False)
    password_for_tournament = models.CharField(
        blank=False,
        verbose_name='Пароль для входа',
        help_text='Придумайте пароль для входа участников в турнир')
    members = models.IntegerField(blank=False)
    start_date_time = models.DateField()
    end_date_time = models.DateField()
    prize_fund = models.IntegerField(blank=False)
    text = models.TextField(
        verbose_name='Текст турнира',
        help_text='Расскажите, какие матчи будет для прогнозов'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='tournaments/',
        blank=True
    )

    class Meta:
        ordering = ['-start_date_time']
    
    def __str__(self):
        # выводим текст поста
        return self.name