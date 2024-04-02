from django.db import models

class User(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    email = models.EmailField(verbose_name="E-mail")
    address = models.CharField(verbose_name="Адрес", max_length=250)