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
    if request.method == 'POST':
            questions=quiz.objects.all()
            score,wrong,correct,total=0,0,0,0
            for q in questions:
                if q.quesno == 1:
                    if q.ans ==  request.POST.get('1'):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                elif q.quesno == 2:
                    if q.ans ==  request.POST.get('2'):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                if q.quesno == 3:
                    if q.ans ==  request.POST.get('3'):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                if q.quesno == 4:
                    if q.ans ==  request.POST.get('4'):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                if q.quesno == 5:
                    if q.ans ==  request.POST.get('5'):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
            context = {
                'score':score,
                'correct':correct,
                'wrong':wrong,
                'total':total
            }
    return render(request,'result.html',context)

def Quiz(request):
    return render(request,'quiz.html',{"ques":quiz.objects.all()})



# <script>
#         function displayRadioValue() {
#             document.getElementById("quizval").innerHTML = "";
#             var ele = document.getElementsByTagName('input');
              
#             for(i = 0; i < ele.length; i++) {
                  
#                 if(ele[i].type="radio") {
                  
#                     if(ele[i].checked)
#                         document.getElementById("quizval").innerHTML
#                                 += ele[i].name + " Value: "
#                                 + ele[i].value + "<br>";
#                 }
#             }
#         }
#     </script>