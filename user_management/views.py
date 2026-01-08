import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_backends
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from abegify.exceptions import http_exception
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status


# Create your views here.
@csrf_exempt
def user_login(request):
    try:
        data = json.loads(request.body)

        email = data.get('email')
        password = data.get('password')
        if not (email and password):
            return JsonResponse({"error":"Email and Password must be supplied."}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(request, username=email, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': token.key, "user":user.as_dict()}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"error":"Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['POST', 'GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def sio_sid(request):
    try:
        data = json.loads(request.body)
        sid = data.get('sid')

        if not sid:
            return JsonResponse({"error": "SID must be supplied."}, status=status.HTTP_400_BAD_REQUEST)
        session = request.session
        session['sio_sid'] = sid
        session.save()
        return JsonResponse({"message": "SID authenticated successfully."}, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)




# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)  # sets session cookie
            return HttpResponse(f"Welcome, {user.email}!")
        else:
            return HttpResponse("Invalid credentials", status=401)

    return render(request, "login.html")
