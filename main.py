
from django.db import models
from django.contrib.auth.models import User

# создаю сущность продукта с полямя: создатель, название, дата старта и цена
class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

#создаю сущьность урока со связью с продуктом, поля: название и ссылка
class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    video_link = models.URLField()

#сущьность группы со списком участников и внешним ключем к продукту, и полями: название, мин и мак количесво пользователей
class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    min_users = models.IntegerField()
    max_users = models.IntegerField()
    members = models.ManyToManyField(User, related_name='groups')

#сущьность описывающая доступ пользователя к курсам
##возможно будет лучше добавить сущьность пользователя с котором хранить всю инфу, в том числе и доступ к продуктам и группам.
class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

