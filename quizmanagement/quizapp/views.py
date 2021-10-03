from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . models import quiz
# Create your views here.

def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]
        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #return render(request,'quiz.html')
            return HttpResponseRedirect(reverse("Quiz"))
            # Otherwise, return login page again with new context
        else:
            return render(request, "login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "login.html")
def logout_view(request):
    logout(request)
    return render(request, "login.html", {
                "message": "Logged Out"
            })

def User(request):
    return render(request,'User.html')

def result(request):
    return render(request,'result.html')

def Quiz(request):
    if request.method == 'POST':
            questions=quiz.objects.all()
            score,wrong,correct,total=0,0,0,0
            for q in questions:
                if q.ans ==  request.POST.get('q.question'):
                    score+=10
                    correct+=1
                else:
                    wrong+=1
            percent = score/(total*10) *100
            context = {
                'score':score,
                'correct':correct,
                'wrong':wrong,
                'percent':percent,
                'total':total
            }
            return render(request,'result.html',context)
    else:
        questions=quiz.objects.all()
        context = {
            'ques':questions
        }
    return render(request,'quiz.html',context)

