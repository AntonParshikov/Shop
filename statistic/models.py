from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Statistic(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок'),
    slug = models.CharField(max_length=100, **NULLABLE, verbose_name='Ссылка'),
    content = models.TextField(**NULLABLE, verbose_name='Содержимое'),
    image = models.ImageField(upload_to='statistic/', **NULLABLE, verbose_name='Превью'),
    creation_date = models.DateField(**NULLABLE, verbose_name='Дата создания'),
    publication_feature = models.BooleanField(default=True, verbose_name='Признак публикации'),
    views_count = models.IntegerField(verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title}: {self.views_count}'

    class Meta:
        verbose_name = 'статистика'
        verbose_name_plural = 'статистики'
