from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from random import randint
import hashlib
import hmac
import base64
import requests
import time
import json
import os

from .serializers import ProfileSerializer, AuthSerializer
from .models import SMS_auth

scriptpath = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
filename = os.path.join(scriptpath, 'secrets.json')
with open(filename) as f:
    secret_data = json.load(f)

User = get_user_model()
access_key = secret_data['ACCESS_KEY']
secret_key_in_json = secret_data['SECRET_KEY']
secret_key = bytes(secret_key_in_json, 'UTF-8')
serviceId = 'ncp:sms:kr:284676110745:sms_auth'
mainURL = 'https://sens.apigw.ntruss.com'
subURL = f"/sms/v2/services/{serviceId}/messages"
sending_phone_number = '01073118189'


@api_view(['GET', 'POST'])
def my_profile(request):
    user = request.user
    if user.profile_image == 0:
        user.profile_image = randint(1, 24)
        user.save()
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        user.nickname = request.data["nickname"]
        user.save()
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def profile_image_update(request, profile_number):
    user = request.user
    user.profile_image = profile_number
    user.save()
    serializer = ProfileSerializer(user)
    return Response(serializer.data) 


@api_view(['GET'])
def is_auth(request):
    pass


@api_view(['POST'])
def sms_send(request, phone_number):
    auth_number = randint(100000, 999999)
    user = request.user
    flag = False
    if user.is_anonymous and request.data['username']:
        user = get_object_or_404(User, username=request.data['username'])
        flag = True
    time_stamp = int(time.time() * 1000) // 1000
    if user.is_anonymous:
        if SMS_auth.objects.filter(phone_number=phone_number).exists():
            auth_model = get_object_or_404(SMS_auth, phone_number=phone_number)
            auth_model.auth_number = auth_number 
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        if SMS_auth.objects.filter(phone_number=phone_number).exists():
            auth_model = get_object_or_404(SMS_auth, phone_number=phone_number)
            if user == auth_model.user:
                auth_model.auth_number = auth_number 
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            if flag:
                return Response(status=status.HTTP_404_NOT_FOUND)
            auth_model = SMS_auth(phone_number=phone_number, auth_number=auth_number, user=user)
    auth_model.time_stamp = time_stamp
    auth_model.is_auth = False
    auth_model.save()
    sms_send_by_naver_cloud(auth_model.phone_number, auth_model.auth_number)
    serializer = AuthSerializer(auth_model)
    return Response(serializer.data)


@api_view(['POST', 'PUT'])
def sms_auth(request, phone_number, auth_number):
    auth_model = get_object_or_404(SMS_auth, phone_number=phone_number)
    result = bool(int(auth_model.auth_number) == int(auth_number))
    user = request.user
    now = int(time.time() * 1000) // 1000
    if request.method == 'POST':
        if result:
            if now - auth_model.time_stamp < 301:
                if user.is_anonymous:
                    user = get_object_or_404(User, phone_number=phone_number)
                    serializer = ProfileSerializer(user)
                    return Response(serializer.data)
                else:
                    user.phone_number = phone_number
                    user.save()
                    auth_model.is_auth = True
                    auth_model.save()
                    serializer = AuthSerializer(auth_model)
                    return Response(serializer.data)
            else:
                auth_model.delete()
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            if user.is_authenticated and now - auth_model.time_stamp > 300:
                auth_model.delete()
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        if user.is_anonymous:
            user = get_object_or_404(User, username=request.data.get('username', ' '))
        if result:
            if now - auth_model.time_stamp < 301:
                auth_model.is_auth = True
                auth_model.save()
                serializer = AuthSerializer(auth_model)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


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


@api_view(['PUT'])
def change_password(request):
    user = get_object_or_404(User, username=request.data.get('username', ' '))
    password = request.data.get('password', ' ')
    if check_password(user.password, password):
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    try:
        user.set_password(password)
        user.save()
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = ProfileSerializer(user)
    return Response(serializer.data) 
