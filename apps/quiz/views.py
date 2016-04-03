from django.http import HttpResponse,  HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import Question, Choice

"""
each app ahs its own urls.py file that stores customeURL patterns
that pointe to methods within the view.py file.

each created urls.py should be registed
via url(r'^quiz/', include('apps.quiz.urls'))
to the main urls.py in the root urls.py file.
"""
def index(request):
    print("in index function")
    """
    render take request object as its first argument, a tempalte name
    as second argument and a dictionary as an optional third argument
    """
  #   context = {
  #     'questions': [
  #          { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
  #          { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
  #          { 'id': 3, 'content': 'Why are they called apartments when they are all together?'},
  #          { 'id': 4, 'content': 'Why are cigarettes sold where smoking is prohibited?'},
  #      ]
  # }
    return render(request, 'quiz/index.html')

def quiz(request):
    print("in quiz function")
    # write a QuerySet to retrieve all the Question objects from our database
    questions = Question.objects.all()
     # package the data in a dictionary to pass to the template
    context = {
         'questions': questions,
     }
    return render(request, 'quiz/quiz.html', context)


def show(request, question_id):
    print("in show function")
    # get the question based on the question_id passed through the request url pattern
    req_question = Question.objects.get(id=question_id)
    # get the choices that belong to the question
    choices = Choice.objects.all().filter(question=req_question)
    # print(req_question)
    # print(choices)
    context = {
        'question': req_question,
        'choices': choices,
    }
    return render(request, 'quiz/show.html', context)
