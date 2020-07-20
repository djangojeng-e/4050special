# Generated by Django 3.0.8 on 2020-07-19 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resource',
            options={'verbose_name': '자료실', 'verbose_name_plural': '자료실'},
        ),
        migrations.AlterField(
            model_name='resourcefiles',
            name='files',
            field=models.FileField(blank=True, upload_to='resources/files/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='resourceimages',
            name='images',
            field=models.ImageField(blank=True, upload_to='resources/images/%Y/%m'),
        ),
    ]