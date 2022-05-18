from django.db import models

class CatMenu(models.Model):
    class Meta():
        ordering = ['cat_menu_name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    cat_menu_name = models.CharField(max_length=40, blank=True, null=True, verbose_name='Имя категории')
     #slug = models.SlugField(verbose_name='slug', null=True, db_index=True, unique=True)
    cat_menu_name_image = models.ImageField(upload_to='image/menu/%Y/%m/%d/', blank=True, null=True, verbose_name='Фото категории меню')


    def __str__(self):
        return self.cat_menu_name

class BaseMenu(models.Model):
    category = models.ForeignKey(CatMenu, on_delete=models.CASCADE, verbose_name='Категория')
    title_menu = models.CharField(max_length=40, blank=True, null=True, verbose_name='Заголовок меню')
    #slug = models.SlugField(verbose_name='slug', null=True, db_index=True, unique=True)
    text_menu = models.TextField(blank=True, null=True, verbose_name='Текст меню')
    image_menu = models.ImageField(upload_to='image/%Y/%m/%d/', blank=True, null=True, verbose_name='фото')

    def __str__(self):
        return self.title_menu