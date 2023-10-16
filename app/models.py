from django.db import models

class Artist(models.Model):
    name = models.CharField('Имя автора', max_length=300, blank=False)

    class Meta:
        verbose_name = 'Артист'
        verbose_name_plural = 'Артисты'

    def __str__(self):
        return str(self.name)


class Album(models.Model):
    name = models.CharField('Название альбома', max_length=300, blank=False)
    artist = models.OneToOneField(Artist, on_delete=models.CASCADE, primary_key=True)
    year = models.PositiveSmallIntegerField('Год', blank=False)

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
    
    def __str__(self):
        return f'{self.name}[{self.year}]'


class Track(models.Model):
    name = models.CharField('Имя автора', max_length=300, blank=False)
    album = models.OneToOneField(Album, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'

    def __str__(self):
        return str(self.name)