from django.shortcuts import render
#from django.http import HttpResponse

def homepage(request):
    #return HttpResponse('This rama ped page!')
    return render(request,'home.html')

def about(request):
    #return HttpResponse('this is rama about page! ')
    return render(request,'about.html')

def doctor(request):
    #return HttpResponse('doctor page ')
    return render(request,'doctor.html')

def laboratory(request):
    #return HttpResponse('laboratory page')
    return render(request,'laboratory.html')
    
def result(request):
    #return HttpReponse('result page')
    return render(request,'result.html')