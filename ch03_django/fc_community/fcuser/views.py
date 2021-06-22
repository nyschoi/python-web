from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import Fcuser

# Create your views here.
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
