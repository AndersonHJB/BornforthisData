from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # 保存用户信息到数据库
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)  # 验证用户信息
            login(request, user)  # 登陆用户
            return redirect('home')  # 重定向到首页
    else:
        form = UserCreationForm()  # 如果不是 POST 请求，创建一个空表单
    return render(request, 'register.html', {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)  # 验证用户信息
            if user is not None:
                login(request, user)  # 登陆用户
                return redirect('home')  # 重定向到首页
            else:
                return redirect('login')  # 登录失败，重定向到登录页面
    else:
        form = AuthenticationForm()  # 如果不是 POST 请求，创建一个空表单
    return render(request, 'login.html', {'form': form})
