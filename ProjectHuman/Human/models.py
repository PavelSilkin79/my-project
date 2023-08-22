from django.db import models
from django.urls import reverse_lazy

class Human(models.Model):
    name = models.CharField(max_length=150, verbose_name='ИМЯ')
    surname = models.CharField(max_length=150, verbose_name='ФАМИЛИЯ')
    age = models.DateTimeField(auto_now=True, verbose_name='ВОЗРАСТ')
    content = models.TextField(blank=True, verbose_name='Резюме')
    address = models.TextField(blank=True, verbose_name='АДРЕС ПРОЖИВАНИЯ')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='ФОТО')
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True, verbose_name='Профессия')

    def get_absolute_url(self):
        return reverse_lazy('View_human', kwargs={'human_id': self.pk})


    class Meta:
        verbose_name = 'человек'
        verbose_name_plural = 'люди'
        ordering = ['age']


class Profession(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Профессия')

    def get_absolute_url(self):
        return reverse_lazy('Profession', kwargs={'profession_id': self.pk})

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        ordering = ['title']


