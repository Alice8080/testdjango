# Generated by Django 4.2.6 on 2023-10-16 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Имя автора')),
            ],
            options={
                'verbose_name': 'Артист',
                'verbose_name_plural': 'Артисты',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('name', models.CharField(max_length=300, verbose_name='Название альбома')),
                ('artist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.artist')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('name', models.CharField(max_length=300, verbose_name='Имя автора')),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.album')),
            ],
            options={
                'verbose_name': 'Трек',
                'verbose_name_plural': 'Треки',
            },
        ),
    ]
