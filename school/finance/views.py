from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def feeCollection(request):
    return render(request,'finance/feeCollection.html')
    # return HttpResponse("I will collect the fee from this views")

def feeDuesReport(request):
    return render(request, 'finance/feeDuesReport.html')
    # return HttpResponse("I will get fee dues report from view")

def feeCollectionReport(request):
    return render(request, 'finance/feeCollectionReport.html')
    # return HttpResponse("I will get fee collection report from this view")