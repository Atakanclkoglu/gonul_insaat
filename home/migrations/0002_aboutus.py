# Generated by Django 5.1.2 on 2024-12-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Başlık')),
                ('heading', models.CharField(max_length=255, verbose_name='Alt Başlık')),
                ('description', models.TextField(verbose_name='Açıklama')),
                ('short_description', models.TextField(blank=True, verbose_name='Kısa Açıklama')),
                ('years_of_experience', models.PositiveIntegerField(verbose_name='Deneyim Yılı')),
                ('image_1', models.ImageField(upload_to='about_images/', verbose_name='Görsel 1')),
                ('image_2', models.ImageField(upload_to='about_images/', verbose_name='Görsel 2')),
                ('read_more_url', models.URLField(blank=True, verbose_name='Daha Fazla Oku Linki')),
            ],
        ),
    ]
