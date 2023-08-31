from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email 

# Create your views here.
class EmailValidationView(View):
    def post(self, request):
        data=json.loads(request.body)
        email=data['email']

        #is username alphanumeric chars
        if not validate_email(email):
            return JsonResponse({'email_error':'email is invalid'}, status=400) 
        #does username exist already?   
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'sorry, email associated with another account already'}, status=409)
        return JsonResponse({'email_valid': True})
    
class UsernameValidationView(View):
    def post(self, request):
        data=json.loads(request.body)
        username=data['username']

        #is username alphanumeric chars
        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphanumeric characters'}, status=400) 
        #does username exist already?   
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'username has already been taken, choose another one'}, status=409)
        return JsonResponse({'username_valid': True})
    
class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

