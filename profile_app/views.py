from django.shortcuts import render

def index(request):	
	return render(request, 'profile_app/index.html')
