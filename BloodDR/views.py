from django.shortcuts import render
from .models import BloodDRList

def index(request):
    return render(request, 'BloodDR/index.html')
def ShowData(request):
    Bloodlist= BloodDRList.objects.all()
    return render(request, 'BloodDR/Showlist.html', {'BloodDRList' : Bloodlist})

def InsertData(request):
    BDName = request.POST.get('BDName')
    Sex= request.POST.get('Sex')
    Age = request.POST.get('Age')
    location = request.POST.get('location')
    BloodGP=request.POST.get('BloodGP')
    Blood_list=BloodDRList(BDName=BDName,Sex=Sex,Age=Age,location=location,BloodGP=BloodGP)
    Blood_list.save()
    return render(request, 'BloodDR/index.html')
