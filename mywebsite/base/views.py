from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.
def home(request):
	if request.method=="POST":
		contact=Contact()
		name=request.POST.get('name')
		email=request.POST.get('email')
		subject=request.POST.get('subject')
		contact.name=name
		contact.email=email
		contact.subject=subject
		contact.save()
		return HttpResponse("<h1>Thanks for Contact</h1>")
	return render(request, 'base/home.html')