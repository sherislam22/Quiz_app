from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
import json

 
# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuisModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total +=1
            
            result =request.POST.get(q.question)
            print(q.ans)
            print(result)
            print()
            if q.ans == result:
                score +=10
                correct +=1
            else:
                wrong +=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':round(percent,2),
            'total':total
        }
        return render(request,'quiz/result.html',context)
    else:
        questions=QuisModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'quiz/home.html',context)
 
def addQuestion(request):    
    if request.user.is_staff:
        form=AddQuestionform()
        if(request.method=='POST'):
            form=AddQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'quiz/addQuestion.html',context)
    else: 
        return redirect('home') 
 
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form = Createuserform()
        if request.method=='POST':
            form = Createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'quiz/register.html',context)
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
       context={}
       return render(request,'quiz/login.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('home')