from django.shortcuts import render

def group_list(request):	
	return render(request, 'groups_app/index.html')
