from django.db import models


# Create your models here.


class Members(models.Model):
    '''
    사용자 모델 
    '''
    name = models.CharField(max_length=50, verbose_name='이름', blank=True)
    birth_date = models.DateField(verbose_name='생년월일', null=True)
    address = models.CharField(max_length=200, verbose_name='주소', blank=True)
    country_residence = models.CharField(max_length=50, verbose_name='거주국가', blank=True)
    occupation = models.CharField(max_length=50, verbose_name='직업 및 대표경력', blank=True)
    nationality = models.CharField(max_length=20, verbose_name="국적", blank=True)
    phone_number = models.CharField(max_length=25, verbose_name='연락처', blank=True)
    email = models.EmailField(max_length=200, verbose_name='이메일', blank=True)
    member_level = models.CharField(max_length=20, verbose_name='해당여부', blank=True)

    password = models.CharField(max_length=40, verbose_name='비밀번호')

    
    def user_name(self):
        user_name = f'{self.name}_{self.country_residence}'
        return user_name

    def __str__(self):
        return f'{self.name}, {self.birth_date}, {self.address}, {self.country_residence}, {self.occupation}, {self.nationality}, {self.phone_number}, {self.email}, {self.member_level}'

    class Meta:
        verbose_name = "4050자문위원"
        verbose_name_plural = "4050자문위원"
