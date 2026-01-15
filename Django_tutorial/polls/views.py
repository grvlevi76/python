from django.shortcuts import render, get_object_or_404, redirect

# Create your views here - changed by goofy
from django.http import HttpResponse ,Http404, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context ={'latest_question_list':latest_question_list,}
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    try:
        question = Question.objects.get(id=question_id)
        context = {'question':question}
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    return render(request,'polls/details.html',context)


def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try: 
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        error_message = "u voted without selecting a choice , pls choose the option"
        context = {'error_message':error_message,'question':question}

        return render(request,'polls/details.html',context)
    else:
        selected_choice.votes = F("votes") +1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/result.html',{'question':question})
