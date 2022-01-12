from django.db import models


class Contact(models.Model):
    """Подписка по email"""
    name = models.CharField(max_length=30, verbose_name='Контакт')
    email = models.EmailField(max_length=50, verbose_name='E-mail')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
