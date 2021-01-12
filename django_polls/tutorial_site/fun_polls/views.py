from django.template import loader

from django.http import HttpResponse, HttpResponseRedirect,Http404

from django.shortcuts import get_object_or_404, render

from django.urls import reverse

from .models import Choice, Question

from django.urls import reverse
from django.views import generic

from .models import Choice, Question


def hello_index(request):
    return HttpResponse("Hello, Team. You're at the polls Index Page.")

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('fun_polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
'''

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'fun_polls/index.html', context)

'''
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
'''



'''
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'fun_polls/detail.html', {'question': question})

'''

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'fun_polls/detail.html', {'question': question})

# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'fun_polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

'''
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
'''

# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'fun_polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('fun_polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'fun_polls/results.html', {'question': question})


class IndexView(generic.ListView):
    template_name = 'fun_polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'fun_polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'fun_polls/results.html'








