from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import UserDetails
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserDetailsSerializer
import json

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('signup')

        user = UserDetails(username=username, email=email, password=password)
        user.save()
        return redirect('login')

    return render(request, 'Loginify/signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = UserDetails.objects.get(email=email)
            if user.password == password:
                messages.success(request, 'Login successful!')
                return render(request, 'success.html', {'user': user})
            else:
                messages.error(request, 'Incorrect password')
        except UserDetails.DoesNotExist:
            messages.error(request, 'Email not registered')
            
        return redirect('login')

    return render(request, 'Loginify/login.html')

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = UserDetails.objects.all()
        serializer = UserDetailsSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = UserDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_detail(request, email):
    try:
        user = UserDetails.objects.get(email=email)
    except UserDetails.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
    if request.method == 'GET':
        serializer = UserDetailsSerializer(user)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = UserDetailsSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
        
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse("Successfully deleted", status=204)
