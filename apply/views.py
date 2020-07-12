from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApplyForm
from .models import Members
from django.contrib.auth.hashers import make_password

# Create your views here.


def index(request):
    return render(request, 'index.html')


def application(request):
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            birth_date = form.cleaned_data['birth_date']
            print(birth_date)
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
            password = make_password(password)
            print(name, birth_date, address, country_residence, occupation, nationality, nationality_country, phone_country_code, phone_number)
            print(email, member_level, password)
            agreement = form.cleaned_data['agreement']
            print(agreement)
            print(re_password)

            try:
                new_member = Members(name=name, birth_date=birth_date, address=address,
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
                return HttpResponse('잘안됬습니다')
    else:
        form = ApplyForm()
    return render(request, 'apply/application.html', {'form': form}) 


def registration(request): 
    name = request.POST['name_value', 'None']
    username = request.POST['username']
    email = request.POST['email']
    country_residence = request.POST['country_residence']
    selection = request.POST['selection']
    message = request.POST['message']
    yes = request.POST['yes']
    no = request.POST['no'] 
    print(name, username, email, country_residence, selection)
    print(message, yes, no)
    return HttpResponse(f'{name}, {username}, {email}, {country_residence}, {selection}, {message}, {yes}, {no}')


def terms_and_conditions(request):
    return render(request, 'apply/terms_and_conditions.html')