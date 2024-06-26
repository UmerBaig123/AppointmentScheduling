from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import userdata,availability
# Create your views here.
@login_required( login_url='login')
def islView(request):
    try:
        this_user_data = userdata.objects.get(user=request.user)
    except userdata.DoesNotExist:
        this_user_data = None
    if request.method == 'POST':
        if this_user_data is None:
            this_user_data = userdata()
            this_user_data.user = request.user
        this_user_data.lastName = request.POST['lastname']
        this_user_data.firstName = request.POST['firstname']
        this_user_data.formEmail = request.POST['email']
        this_user_data.passportNumber = request.POST['passportnumber']
        this_user_data.citizenship = request.POST['citizenship']
        this_user_data.telephone = request.POST['telephone']
        this_user_data.visaCategory = request.POST['visacategory']
        this_user_data.save()
    return render(request, 'islamabad.html',{'old_email':request.user.email,'userdata':this_user_data})
def krView(request):
    try:
        this_user_data = userdata.objects.get(user=request.user)
    except userdata.DoesNotExist:
        this_user_data = None
    if request.method == 'POST':
        if this_user_data is None:
            this_user_data = userdata()
            this_user_data.user = request.user
        this_user_data.lastName = request.POST['lastname']
        this_user_data.firstName = request.POST['firstname']
        this_user_data.formEmail = request.POST['email']
        this_user_data.passportNumber = request.POST['passportnumber']
        this_user_data.citizenship = request.POST['citizenship']
        this_user_data.telephone = request.POST['telephone']
        this_user_data.visaCategory = request.POST['visacategory']
        this_user_data.save()
    return render(request, 'islamabad.html',{'old_email':request.user.email,'userdata':this_user_data})
def home(request):
    return render(request, 'home.html') 
class checkAvailability(APIView):
    def get(self, request):
        allavailability = availability.objects.all()
        if len(allavailability)== 0:
            return Response({'availability': False})
        return Response({'availability': allavailability[0].url})
    def post(self, request):
        availability.objects.all().delete()