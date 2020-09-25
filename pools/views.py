# from django.shortcuts import render
#
# def inddex(request):
#     return render(request,'不是井里没水，而是挖的不够深')

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# from django.http import Http404
# from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    # template = loader.get_template('pools/index.html')
    # return HttpResponse(template.render(context, request))

    return render(request, 'pools/index.html', context)


# 问题详情页
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Qestion does not exist')
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'pools/detail.html', {'question': question})



# 投票结果页
def results(request, question_id):
    response = 'You are looing at the results of question %s'
    return HttpResponse(response % question_id)


# 问题投票页
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
