from django.db import models

class Artist(models.Model):
    name = models.CharField('Name', max_length=300, blank=False)

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        return str(self.name)


class Album(models.Model):
    name = models.CharField('Title', max_length=300, blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField('Year', blank=False)

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
    
    def __str__(self):
        return f'{self.name}[{self.year}]'


class Track(models.Model):
    name = models.CharField('Title', max_length=300, blank=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'

    def __str__(self):
        return str(self.name)