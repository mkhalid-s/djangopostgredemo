from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.urls import reverse
import os

# Create your views here.


# def index(request):
#     # return HttpResponse("Hi! , Welcome to index Page of Polls")
#     latest_question = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question])
#     base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     return HttpResponse(output + ' ' + base_path)

def index(request):
    latest_question = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question,
    }
    return HttpResponse(template.render(context, request))


# def detail(request, question_id):
#     # try:
#         question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist as e:
#     #     raise Http404('Question doesnt Exist '.join(e))

#         template = loader.get_template("polls/detail.html")
#         return HttpResponse(template.render({'question': question}, request))
#     #    return render(request, 'polls/detail.html', {'question': question})
#     # return HttpResponse("You'r looking at question %s." % question_id)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        return render(request, 'polls/detail.html', {'question': question})
    except Question.DoesNotExist as e:
        raise Http404('Question doesnt Exist ')


# def results(request, question_id):
#     response = "You are loooking at the results of question %s."
#     return HttpResponse(response % question_id)


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist) as e:
        return render(request, "polls/detail.html", {
            'question': question,
            'error_message': "You didn't select a vote choice", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {'question': question})
