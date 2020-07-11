from django.forms import ModelForm
from django import forms
from .models import Members
import datetime 
from django_countries.fields import CountryField


class ApplyForm(forms.Form):
    
    name = forms.CharField(required=True,  
        error_messages={
            'required': '성함을 다시 입력해주세요'
        },
        max_length=50, label="성명", widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': '성함을 입력해주세요',
            }
        )
    )
    
    birth_date = forms.DateField(required=True,
        error_messages={
            'required': '생년월일을 YYYY-MM-DD 형태로 입력해주세요',
            'invalid': '생년월일을 YYYY-MM-DD 형태로 입력해주세요'
        },
    widget=forms.DateInput(
        attrs={
            'class': 'input',
            'id': 'from-datepicker',
            'placeholder': 'YYYY-MM-DD 생년월일을 입력해주세요',
        }
    ), label="생년월일"
    )

    address = forms.CharField(required=True,
    max_length=200,
    error_messages= {
        'required': '주소를 입력해주세요'
    },
    widget=forms.TextInput(
        attrs={
            'class': 'input',
            'placeholder': '주소를 입력해주세요'
        }
    )
    )

    country_residence = CountryField(blank=False, 
    error_messages={'required': '거주 국가를 입력해주세요'},).formfield(label="거주국가", initial="KR",
        widget=forms.Select(attrs={'class': 'input', 'placeholder': '거주국가를 입력하세요'}))

    occupation = forms.CharField(max_length=50, label="직업 및 경력사항", widget=forms.TextInput(
        attrs={
            'class': 'input',
            'placeholder': '직업 및 경력사항을 입력해주세요',
        }
    ) )

    nationalities = (
        ('대한민국', '대한민국'),
        ('외국인', '외국인')
    )

    nationality = forms.ChoiceField(choices=nationalities, required=True, label='국적상태', 
    widget= forms.Select(attrs={'class': 'input'}))

    nationality_country = CountryField(blank=True, error_messages={'required': '소지하신 국적 국가를 입력해주세요'}).formfield(
        label='외국인인 경우 소지국적 선택', initial='KR', widget=forms.Select(attrs={'class': 'input', 'placeholder': '국적을 선택하세요'})
    )
    
    phone_country_code = forms.CharField(max_length=10, required=True,
    error_messages={'required': '국가번호를 입력해주세요'}, label="연락처 국가번호", 
    widget=forms.TextInput(attrs={'class': 'input', 'placeholder': '국가번호를 입력해주세요'}))
    
    phone_number = forms.CharField(max_length=30, required=True, label="전화번호",
    error_messages={'required': '전화번호를 입력해주세요'}, 
    widget=forms.TextInput(attrs={'class': 'input', 'placeholder': '전화번호를 입력해주세요'}))
    
    email = forms.EmailField(required=True, label="Email (이메일 주소)",
    error_messages={'required': '정확한 이메일 형식을 입력해주세요'},
    widget=forms.EmailInput(
        attrs={'class':'input', 'placeholder': '이메일을 입력해주세요'}))
    
    

    password = forms.CharField(required=True, label="비밀번호",
    widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': '비밀번호를 입력해주세요'}))

    re_password = forms.CharField(required=True, label="비밀번호 재입력",
    widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': '비밀번호를 다시 입력해주세요'}))

    members_levels = (
        ('대의원', '대의원'),
        ('권리당원', '권리당원'),
        ('당원', '당원'),
        ('없음', '해당없음')
    )

    member_level = forms.ChoiceField(choices=members_levels, label="당원여부 (선택사항)", 
    required=False, initial='없음', 
    widget=forms.Select(attrs={'class': 'input', 'placeholder': '당원 여부를 선택해주세요', 'id':'selection'}))

    

        
