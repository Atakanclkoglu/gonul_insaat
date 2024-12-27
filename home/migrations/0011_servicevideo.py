# Generated by Django 5.1.2 on 2024-12-25 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Başlık')),
                ('video', models.FileField(upload_to='videos/', verbose_name='Video Dosyası')),
                ('logo', models.ImageField(upload_to='logos/', verbose_name='Logo Görseli')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
            ],
            options={
                'verbose_name': 'Hizmet Videosu',
                'verbose_name_plural': 'Hizmet Videoları',
            },
        ),
    ]
