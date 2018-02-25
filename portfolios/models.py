# coding: utf-8
from django.db import models

class PersonalData(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    adress = models.CharField(max_length=100, verbose_name="Ubicación")
    city = models.CharField(max_length=50, verbose_name="Ciudad")
    postal_code = models.CharField(max_length=10, verbose_name="Postal Code")
    phone = models.CharField(max_length=20, verbose_name="Telefono")
    mobile = models.CharField(max_length=20, verbose_name="Celular")

    about = models.TextField(max_length=255, verbose_name="Sobre")
    birth_date = models.CharField(max_length=50, default=' 01 enero 2000',verbose_name="Fecha Nacimiento")
    email = models.EmailField(verbose_name="Email")

    knowledge = models.CharField(max_length=50, verbose_name="Conocimientos")
    github = models.CharField(max_length=100,default='https://github.com/YourGithub ', verbose_name="Github")
    current_position = models.CharField(max_length=50, verbose_name="Empleo Actual")
    companie = models.CharField(max_length=50, verbose_name="Empresa")

    def __str__ (self):
        return self.name


