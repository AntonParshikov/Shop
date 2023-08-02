from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=250, **NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, **NULLABLE, on_delete=models.CASCADE, verbose_name='Категория')
    purchase_price = models.IntegerField(**NULLABLE, verbose_name='Цена за покупку')
    creation_date = models.DateField(**NULLABLE, verbose_name='Дата создания')
    last_mode_date = models.DateField(**NULLABLE, verbose_name='Дата последнего изменения')
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} : {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    version_number = models.IntegerField(verbose_name='номер версии')
    version_title = models.CharField(max_length=150, verbose_name='название версии')
    sign_current_version = models.BooleanField(default=True, verbose_name='признак текущей версии')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    def __str__(self):
        return f'{self.version_title}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
