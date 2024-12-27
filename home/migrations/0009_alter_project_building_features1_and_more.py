# Generated by Django 5.1.2 on 2024-12-25 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_project_building_features_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='building_features1',
            field=models.TextField(blank=True, default='', help_text='Bina ile ilgili özellikler.', max_length=100, null=True, verbose_name='Bina Özelliği 1'),
        ),
        migrations.AlterField(
            model_name='project',
            name='building_features2',
            field=models.TextField(blank=True, default='', help_text='Bina ile ilgili özellikler.', max_length=100, null=True, verbose_name='Bina Özelliği 2'),
        ),
        migrations.AlterField(
            model_name='project',
            name='building_features3',
            field=models.TextField(blank=True, default='', help_text='Bina ile ilgili özellikler.', max_length=100, null=True, verbose_name='Bina Özelliği 3'),
        ),
        migrations.AlterField(
            model_name='project',
            name='building_name',
            field=models.CharField(blank=True, default='', help_text='Projede yer alan bina adı.', max_length=200, null=True, verbose_name='Bina Adı'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_description',
            field=models.TextField(blank=True, help_text='Proje hakkında açıklama.', null=True, verbose_name='Proje Açıklaması'),
        ),
    ]
