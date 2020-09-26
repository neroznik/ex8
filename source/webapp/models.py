from django.contrib.auth import get_user_model
from django.db import models

DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = (
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', 'Продукты питания'),
    ('household', 'Хоз. товары'),
    ('toys', 'Детские игрушки'),
    ('appliances', 'Бытовая Техника')
)
CHOICES = [(i,i) for i in range(6)]


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    category = models.CharField(max_length=20, verbose_name='Категория',
                                choices=CATEGORY_CHOICES, default=DEFAULT_CATEGORY)
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    photo = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Картинка')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1,
                               related_name='comments', verbose_name='Автор')
    product =models.ForeignKey('webapp.Product', related_name='products',
                                on_delete=models.CASCADE, verbose_name='Продукт')
    review = models.TextField(verbose_name='Отзыв')
    rate = models.IntegerField(choices=CHOICES, unique=True)

    def __str__(self):
        return f'{self.author}: {self.review}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

