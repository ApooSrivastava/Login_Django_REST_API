from django.shortcuts import render
# from rest_framework.authtoken import Token
from django.template.base import Parser, Token
# from django.contrib.auth.models import user 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.authtokens.views import obtain_auth_tokens
from django.contrib.auth import login, authenticate
# Create your views here.


class Login(APIView):
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Please fill all the fields"}, status = status.HTTP_400_BAD_REQUEST)
        
        check_user = user.objects.filter(username = username).exists()
        if check_user == False:
            return Response({"error": "Username does not exists"}, status = status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            token,created = Token.object.get_or_created(user=request.user)

            data = {
                'token': token.key,
                'user_id': request.user.pk,
                'username': request.user.username
            }

            return Response({"success":"succesful login"}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"Invalid Login Details"}, status=status.HTTP_400_BAD_REQUEST)