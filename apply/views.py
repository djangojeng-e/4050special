from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ApplyForm, LoginForm
from .models import Members
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
# csv export 
import csv


# Create your views here.


def index(request):
    return render(request, 'index.html')


def application(request):
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            nick_name = form.cleaned_data['nick_name']
            birth_date = form.cleaned_data['birth_date']
            address = form.cleaned_data['address']
            country_residence = form.cleaned_data['country_residence']
            occupation = form.cleaned_data['occupation']
            nationality = form.cleaned_data['nationality']
            nationality_country = form.cleaned_data['nationality_country']
            phone_country_code = form.cleaned_data['phone_country_code']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            member_level = form.cleaned_data['member_level']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            agreement = form.cleaned_data['agreement']
            if password != re_password:
                return HttpResponse('<script>alert("비밀번호가 서로 일치하지 않습니다."); window.history.back();</script>')
            elif Members.objects.filter(email=email).exists():
                return HttpResponse('<script>alert("이미 존재하는 이메일입니다."); window.history.back();</script>')
            elif Members.objects.filter(nick_name=nick_name).exists():
                return HttpResponse('<script>alert("이미 존재하는 닉네임 입니다."); window.history.back();</script>')
            else:
                password = make_password(password)
            try:
                new_member = Members(name=name, nick_name=nick_name, birth_date=birth_date, address=address,
                                    country_residence=country_residence,
                                    occupation=occupation,
                                    nationality=nationality,
                                    nationality_country=nationality_country,
                                    phone_country_code=phone_country_code,
                                    phone_number=phone_number,
                                    email=email,
                                    member_level=member_level,
                                    password=password)
                new_member.save()
            except: 
                return HttpResponse('문제가 생겼습니다. 사이트 관리자에 문의해주세요.')
            
            # 가입 사용자를 생성후 곧바로 로그인 처리 
            if request.user.is_authenticated:
                return HttpResponse('이미 로그인 되어 있습니다')
            else:
                created_member = Members.objects.get(email=email)
                nickname = created_member.nick_name
                user = User.objects.create_user(username=nickname, email=email, password=password)
                user = authenticate(request, username=nickname, email=email, password=password)
                if user:
                    login(request, user)
                    return redirect('/')
    else:
        form = ApplyForm()
    return render(request, 'apply/application.html', {'form': form}) 


def login_view(request): 
    if request.method == 'POST': 
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.get(email=email)
            username = user.username
            member = Members.objects.get(email=email)
            username = member.nick_name
            password = member.password
            user = authenticate(request, username=username, email=email, password=password)
            if user:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponse('''<script>alert("로그아웃 되었습니다"); window.location.href = "/"; </script>''')


def terms_and_conditions(request):
    return render(request, 'apply/terms_and_conditions.html')


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="members.csv"'
    writer = csv.writer(response)
    writer.writerow(['이름', '사용자닉네임', '생년월일', '주소', 
                     '거주국가', '직업/경력', '국적',
                     '국적소지국가', '국가번호',
                     '전화번호',
                     '이메일',
                     '당원여부',
                     '위원회 임원여부'])
    members = Members.objects.all().values_list(
        'name', 'nick_name', 'birth_date', 'address', 
        'country_residence', 'occupation', 'nationality',
        'nationality_country', 'phone_country_code',
        'phone_number',
        'email',
        'member_level',
        'is_member_staff'
    )
    for member in members:
        writer.writerow(member)
    return response

