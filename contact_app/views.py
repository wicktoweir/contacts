from django.shortcuts import render

def contact_list(request):	
	return render(request, 'contact_app/index.html')