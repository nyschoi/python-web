from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser

# Create your views here.


def home(request):
    user_id = request.session.get('user')
    # print(type(request))
    # print(type(Fcuser), type(Fcuser.objects), type(Fcuser.objects.get()))
    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)
    return HttpResponse('Home')


def register(request):
    # 그냥 들어온 경우(get)
    # 등록 버튼을 눌러서 들어온 경우(post)
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        res_data = {}
        if not (username and password and re_password and useremail):
            res_data['error'] = '뭐라도 입력해라'
        elif password != re_password:
            res_data['error'] = '비번이 다르빈!다'
        else:
            fcuser = Fcuser(
                username=username, useremail=useremail, password=make_password(password)
            )
            fcuser.save()
        return render(request, 'register.html', res_data)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        res_data = {}
        if not (username and password):
            res_data['error'] = 'iput!'
        else:
            fcuser = Fcuser.objects.get(username=username)
            if check_password(password, fcuser.password):
                # session
                print(type(request), request.session)
                request.session['user'] = fcuser.id
                # redirect to home
                return redirect('/')
                pass
            else:
                res_data['error'] = 'wrong password'
        return render(request, 'login.html', res_data)


def logout(request):
    if request.session.get('user'):
        del request.session['user']
    return redirect('/')