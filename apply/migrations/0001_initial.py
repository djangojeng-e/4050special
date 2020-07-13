# Generated by Django 3.0.8 on 2020-07-13 05:40

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='이름')),
                ('birth_date', models.DateField(null=True, verbose_name='생년월일')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='주소')),
                ('country_residence', django_countries.fields.CountryField(max_length=2, verbose_name='거주 국가')),
                ('occupation', models.CharField(blank=True, max_length=50, verbose_name='직업 및 대표경력')),
                ('nationality', models.CharField(blank=True, choices=[('대한민국', '대한민국'), ('외국인', '외국인')], max_length=20, verbose_name='국적상태')),
                ('nationality_country', django_countries.fields.CountryField(max_length=2, verbose_name='국적')),
                ('phone_country_code', models.CharField(blank=True, max_length=10, verbose_name='국가번호')),
                ('phone_number', models.CharField(blank=True, max_length=30, verbose_name='전화번호')),
                ('email', models.EmailField(blank=True, max_length=200, verbose_name='이메일')),
                ('member_level', models.CharField(blank=True, choices=[('대의원', '대의원'), ('권리당원', '권리당원'), ('당원', '당원')], max_length=20, verbose_name='해당여부')),
                ('password', models.CharField(max_length=50, verbose_name='비밀번호')),
                ('is_member_staff', models.BooleanField(null=True, verbose_name='임원여부')),
            ],
            options={
                'verbose_name': '4050자문위원',
                'verbose_name_plural': '4050자문위원',
            },
        ),
    ]
