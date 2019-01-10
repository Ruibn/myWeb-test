from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# from django.template import loader

from .models import Question, Choice

# 删除老index，detail和results 视图，并使用Django的通用视图代替，可大大减少代码量，老式可查看浏览器的收藏页


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions.
        (not including those set to published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


# 应该给 ResultsView 也增加一个类似的 get_queryset 方法，并且为它创建测试
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# 此处的vote代码未实现互斥访问，日后可用F()实现
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # request.POST是一个类似字典的对象，允许您按键名访问提交的数据，Django也提供request.GET了以相同方式访问GET数据。
        # 在这种情况下， request.POST['choice']返回所选选项的ID，作为字符串。request.POST值始终是字符串
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You did not select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # 使用构造reverse()函数中的 HttpResponseRedirect函数。
        # 此功能有助于避免在视图功能中对URL进行硬编码。
        # 它给出了我们想要将控制权传递给的视图的名称以及指向该视图的URL模式的可变部分。
        # 此reverse()调用将返回一个类似'/polls/3/results/'的字符串
    # return HttpResponse("You're voting on question %s" % question_id)
