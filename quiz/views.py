from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Question, Deleted
def home(request):
    TotalQuestions = Question.objects.all()
    DeletedQuestions = Deleted.objects.all()
    delQ = len(DeletedQuestions)
    length = len(TotalQuestions)
    add="Add"
    head="Quiz App"
    if request.method == "POST":
        question = request.POST['question']
        solution = request.POST['solution']
        question = Question(question = question, answer = solution)
        question.save()
        messages.success(request, 'Your question has successfully been saved')
        return redirect("/")
    

        


    
    context={
        'heading':head,
        "add":add,
        "length":length,
        "delQ":delQ
    }


    return render(request, 'quiz/index.html', context)


def show(request):
    Tques = Question.objects.all()
    check=""
    if Tques:
        check="Questions"

    else:
        check ="No questions to display"
    
    context ={
    'questions':Tques,
    'check':check
    }

    return render(request, "quiz/show.html", context)


def deleteques(request, pk):
    question = Question.objects.get(id=pk)
    deleted = Deleted(question = question.question, answer = question.answer)
    deleted.save()
    question.delete()
    messages.error(request, 'Your question is deleted temporarily')
    return redirect("show")


def Updateques(request, pk):
    change="Update"
    upd = "Update Question"
    quesObj = Question.objects.get(id=pk)
    if request.method =="POST":
        quesObj.question = request.POST['question']
        quesObj.answer = request.POST['solution']
        quesObj.save()
        messages.success(request, 'Your question has successfully been updated')
        return redirect("/")
    
    context={
        'update':upd,
        'question':quesObj,
        'change':change
    }
    return render(request, 'quiz/index.html', context)



def SearchQuestion(request):
    search=""
    count = ""
    nores=""
    query = request.GET.get('query')
    length = len(query)
    
    questions = Question.objects.filter(Q(question__contains = query)| Q(answer__contains = query))
    queslen = len(questions)
    if length < 40:
        search = "Your search result"
    
        if queslen == 0:
                nores = "No result found"

    if length > 40 and queslen==0:
        count = "yes"



    
    context = {
        "nores":nores,
        "search":search,
        "questions":questions,
        "query":query,
        "length":length,
        "count": count,
    }

    return render(request, 'quiz/searchresult.html', context)


def ShowDelQues(request):
    questions = Deleted.objects.all()
    check =""
    if questions:
        check="Deleted Questions"

    else:
        check ="No deleted questions"

    context={
        'questions':questions,
        'check':check
    }
    return render(request, 'quiz/deletedQues.html', context)

def RestoreQues(request, pk):
    question = Deleted.objects.get(id=pk)
    restoredQues = Question(question = question.question, answer = question.answer)
    restoredQues.save()
    question.delete()
    messages.success(request, 'Question restored successfully')
    return redirect('ShowDelQues')

def permDel(request, pk):
    question = Deleted.objects.get(id=pk)
    question.delete()
    messages.error(request, 'Your question is deleted permanently')
    return redirect("ShowDelQues")







            
            


        



