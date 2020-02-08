from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect, JsonResponse
from .models import Question, Choice
from django.urls import reverse

# Create your views here.
# Query all questions and display
def index(request):
  question_lists = Question.objects.all().order_by('-pub_date')
  context = {
    'question_lists': question_lists
  }
  return render(request, 'polls/index.html', context)


# Query specific question and its choices
def details(request, question_id):
  try:
    question = Question.objects.get(id=question_id)
    choices = question.choice_set.all()
  except Question.DoesNotExist:
    raise Http404('Sorry the question does not exist ')

  context = {
    'question': question,
    'choices': choices
  }
  return render(request, 'polls/details.html', context)


#Vote a specific question choices
def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  choices = question.choice_set.all()

  try:
    selected_choice = choices.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/details.html', {
      'question':question,
      'choices':choices,
      'error_message':'You did not select a choice',
      })
  else:
    selected_choice.votes +=1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
  
  question = get_object_or_404(Question, pk=question_id)
  choices = question.choice_set.all()

  context = {
    'question': question,
    'choices': choices
  }
  return render(request, 'polls/results.html', context)


def resultData(request, question_id):
  choiceData = []
  question = get_object_or_404(Question, pk=question_id)
  choices = question.choice_set.all()

  for choice in choices:
    choiceData.append({choice.choice_text:choice.votes})

  return JsonResponse(choiceData, safe=False)