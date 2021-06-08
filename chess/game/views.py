
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from . import models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Game
from django.http import HttpResponseRedirect
from django.urls import reverse

def game(request, game_id):
    game = get_object_or_404(Game,pk=game_id)
    if request.user != game.owner:
        if game.opponent == None:
            game.opponent = request.user
            game.save()
        elif game.opponent != request.user:
            messages.add_message(request, messages.ERROR, "This game already has enough participants. Try joining another")
            return JsonResponse({
                    "status": 1,
                    "message": "wrong",
                })
    return JsonResponse({
                    "status": 0,
                    "message": "Success",
                })



@require_http_methods(["POST"])
def login_user(request):
    islogin=False
    if request.method == "POST":
        data = json.loads(request.body)
        userid = data.get("username")
        password = data.get("password")
        if userid is not None and password is not None:
            try:
                user = models.User.objects.get(user_id=userid)
                print(password)
                print(user.password)
                if user.password == password:
                    return JsonResponse({
                        "status": 0,
                        "message": "Login Success",
                        "username": user.name,
                    })
                else:
                    return JsonResponse({
                    "status": 1,
                    "message": "登录失败, 请检查密码是否输入正确."
                })
            except:
                return JsonResponse({
                    "status": 1,
                    "message": "登录失败, 请检查用户名是否输入正确."
                })
        else:
            return JsonResponse({
                "status": 2,
                "message": "参数错误"
            })


def register(request):
    if request.method == "POST":
        # data = json.loads(request.body.decode('utf-8'))
        if request.GET.get("select") is not None:
            print(2)
            select_username = request.POST.get("select_username")
            print(select_username)
            try:
                models.User.objects.get(user_id=select_username)
                return JsonResponse({
                    "status": 0,
                    "is_indb": 1
                })
            except:
                return JsonResponse({
                    'status': 0,
                    "is_indb": 0
                })
        username = request.POST.get("name")
        password = request.POST.get("password")
        email = request.POST.get("email")
        userid=request.POST.get("userid")
        gender=request.POST.get("gender")
        print(username)
        print(password)
        print(email)
        print(userid)
        print(gender)
        if userid is not None and password is not None and email is not None  and username is not None and gender is not None:
            try:
                user=models.User()
                user.user_id=userid
                user.password=password
                user.email=email
                user.gender=gender
                user.name=username
                user.save()
                return JsonResponse({
                    "status": 0,
                    "message": "Register Success"
                })
            except:
                return JsonResponse({
                    "status": 2,
                    "message": "注册失败, 该用户已经存在."
                })

    else:
        return JsonResponse({
            "status": 1,
            "message": "error method"
        })


