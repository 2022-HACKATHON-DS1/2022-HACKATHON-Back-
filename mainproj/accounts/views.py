from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
    if request.method == "POST":
        userid = request.POST.get("ID", "Guest (or whatever)")
        pwd = request.POST.get("PASSWORD", "Guest (or whatever)")
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            return render(request, 'login.html')

    # GET 요청: login form을 담고 있는 login.html을 띄우는 역할.
    else:
        return render(request, 'login.html')

def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        # password와 confirm에 입력된 값이 같다면
        if request.POST.get("PASSWORD", "Guest (or whatever)") == request.POST.get("Confirm PW", "Guest (or whatever)"):
            # user 객체를 새로 생성
            user = User.objects.create_user(username=request.POST.get("ID", "Guest (or whatever)"), password=request.POST.get("PASSWORD", "Guest (or whatever)"))
            # 로그인 한다
            auth.login(request, user)
            return render(request, 'login.html')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'signup.html')

def home(request):
    return render(request, 'home.html')