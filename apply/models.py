from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Members(models.Model):
    '''
    사용자 모델 
    '''
    name = models.CharField(max_length=50, verbose_name='이름', blank=True)
    nick_name = models.CharField(max_length=50, verbose_name="닉네임", blank=True)
    birth_date = models.DateField(verbose_name='생년월일', null=True)
    address = models.CharField(max_length=200, verbose_name='주소', blank=True)
    country_residence = CountryField(verbose_name="거주 국가")
    occupation = models.CharField(max_length=50, verbose_name='직업 및 대표경력', blank=True)

    nationalities = (
        ('대한민국', '대한민국'),
        ('외국인', '외국인')
    )

    nationality = models.CharField(max_length=20, choices=nationalities, verbose_name="국적상태", blank=True)
    nationality_country = CountryField(verbose_name="국적")
    phone_country_code = models.CharField(max_length=10, verbose_name='국가번호', blank=True)
    phone_number = models.CharField(max_length=30, verbose_name='전화번호', blank=True)
    email = models.EmailField(max_length=200, verbose_name='이메일', blank=True)

    members_levels = (
        ('대의원', '대의원'),
        ('권리당원', '권리당원'),
        ('당원', '당원')
    )

    member_level = models.CharField(max_length=20, choices=members_levels, verbose_name='해당여부', blank=True)

    password = models.CharField(max_length=50, verbose_name='비밀번호')

    is_member_staff = models.BooleanField(null=True, verbose_name='임원여부')


    def user_name(self):
        user_name = f'{self.name}_{self.country_residence}'
        return user_name

    def __str__(self):
        return f'{self.nick_name}'

    class Meta:
        verbose_name = "4050자문위원"
        verbose_name_plural = "4050자문위원"
