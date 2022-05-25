from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from random import randint
import hashlib
import hmac
import base64
import requests
import time
import json

from .serializers import ProfileSerializer, AuthSerializer
from .models import SMS_auth

User = get_user_model()
access_key = "XVMuf9Nx8OkCQ3ApDCAI"
secret_key = bytes("BjEzWWEpBAhaK51BKq8c8786LAUcK1KeTE9517NQ", 'UTF-8')
serviceId = 'ncp:sms:kr:284676110745:sms_auth'
mainURL = 'https://sens.apigw.ntruss.com'
subURL = f"/sms/v2/services/{serviceId}/messages"
sending_phone_number = '01073118189'


@api_view(['GET', 'POST'])
def my_profile(request):
    user = request.user
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        user.nickname = request.data["nickname"]
        user.save()
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def profile_image(request):
    pass


@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def is_auth(request):
    pass


@api_view(['POST'])
def sms_send(request, phone_number):
    auth_number = randint(100000, 999999)
    if SMS_auth.objects.filter(phone_number=phone_number).exists():
        auth_model = get_object_or_404(SMS_auth, phone_number=phone_number)
        auth_model.auth_number = auth_number
    else:
        auth_model = SMS_auth(phone_number=phone_number, auth_number=auth_number)
    auth_model.is_auth = False
    auth_model.save()
    sms_send_by_naver_cloud(auth_model.phone_number, auth_model.auth_number)
    serializer = AuthSerializer(auth_model)
    return Response(serializer.data)


@api_view(['POST'])
def sms_auth(request, phone_number, auth_number):
    auth_model = get_object_or_404(SMS_auth, phone_number=phone_number)
    auth_model.is_auth = bool(int(auth_model.auth_number) == int(auth_number))
    serializer = AuthSerializer(auth_model)
    return Response(serializer.data)


def make_signature(timestamp):
    method = "POST"
    message = method + " " + subURL + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
    return signingKey


def sms_send_by_naver_cloud(phone_number, auth_number):
    timestamp = str(int(time.time() * 1000))
    params = {
        "type": "SMS",
        "from": sending_phone_number,
        "content": f'인증 번호 [{auth_number}]를 입력해주세요.',
        "messages": [
            {
                "to": phone_number,
            }
        ],       
    }
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "x-ncp-apigw-timestamp": timestamp,
        "x-ncp-iam-access-key": access_key,
        "x-ncp-apigw-signature-v2": make_signature(timestamp)        
    }
    response = requests.post(mainURL + subURL, data=json.dumps(params), headers=headers)
    return response.json()