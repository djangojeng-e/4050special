# Generated by Django 3.0.8 on 2020-07-11 10:29

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0002_auto_20200711_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='is_member_staff',
            field=models.BooleanField(null=True, verbose_name='임원여부'),
        ),
        migrations.AlterField(
            model_name='members',
            name='country_residence',
            field=django_countries.fields.CountryField(max_length=2, verbose_name='거주 국가'),
        ),
        migrations.AlterField(
            model_name='members',
            name='nationality',
            field=models.CharField(blank=True, choices=[('대한민국', '대한민국'), ('외국인', '외국인')], max_length=20, verbose_name='국적상태'),
        ),
        migrations.AlterField(
            model_name='members',
            name='nationality_country',
            field=django_countries.fields.CountryField(max_length=2, verbose_name='국적'),
        ),
        migrations.AlterField(
            model_name='members',
            name='phone_country_code',
            field=models.CharField(blank=True, max_length=10, verbose_name='국가번호'),
        ),
    ]