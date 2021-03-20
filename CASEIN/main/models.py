from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Articles(models.Model):
    title = models.CharField('Имя', max_length=50)
    anons = models.CharField('Мероприятие', max_length=250)
    full_text = models.TextField('Обратная связь')
    date = models.DateTimeField('Дата отправки')


class Members(User):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    dolznost = models.CharField('Должность', max_length=50)
    Zadanie1 = models.CharField('Задание 1', max_length=20, blank=True, default='-')
    Zadanie2 = models.CharField('Задание 2', max_length=20, blank=True, default='-')
    Zadanie3 = models.CharField('Задание 3', max_length=20, blank=True, default='-')
    Zadanie4 = models.CharField('Задание 4', max_length=20, blank=True, default='-')
    zp = models.CharField('Заработная плата', max_length=20)

    def get_absolute_url(self):
        return f'/{self.id}'

    def __str__(self):
        return f'Сотрудник: {self.name} {self.surname}'

    class Meta:
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'


def __str__(self):
	return self.title