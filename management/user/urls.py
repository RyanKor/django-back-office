
from django.urls import path, include
from . import views
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # 기존에 장고 내부에 있던 로그인, 로그아웃과 관련한 페이지 url을 가져온다.
    path('signup', views.signup, name="signup"),
]
