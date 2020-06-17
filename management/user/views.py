from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm  # new contents


# 로그인 관련 라이브러리
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():  # 기본 유효성 검사
            new_user = User.objects.create_user(**form.cleaned_data)
            # cleaned_data 원래 Django에서 사용하는 모듈
            # 유저 모델의 경우, dictionary 파이썬 모델로 생성됩니다.
            # {"username" : password}
            auth.login(request, new_user,
                       backend='django.contrib.backends.ModelBackend')
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'registration/signup.html', {"form": form})
