from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from . import models
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


def index(request):
    bbs_list = models.BBS.objects.all()
    return render_to_response('index.html', {'bbs_list': bbs_list, 'user': request.user})


def bbs_detail(request, bbs_id):
    bbs = models.BBS.objects.get(id=bbs_id)
    return render_to_response('bbs/bbs_detail.html', {'bbs_obj': bbs, 'user': request.user})


def sub_comment(request):
    print(request.POST)
    bbs_id = request.POST.get('bbs_id')
    comment = request.POST.get('comment')

    models.comments.objects.create(
        content_type=13,
        object_pk=bbs_id,
        site_id=1,
        user=request.user,
        comment=comment,
    )

    return HttpResponseRedirect('/detail/%s' % bbs_id)


def bbs_sub(request):
    content = request.POST.get('content')
    author = models.BBS_user.objects.get(user__username=request.user)
    models.BBS.objects.create(
        title='TEST TITLE',
        summary='HAHA',
        content=content,
        author=author,
        view_count=1,
        ranking=1,
    )
    return HttpResponse('yes.')


def bbs_pub(request):
    return render_to_response('bbs/bbs_pub.html', {'user': request.user})
