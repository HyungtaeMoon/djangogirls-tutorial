from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-id')
    context = {
        'posts': posts,
    }
    # render는 주어진 인수를 사용해서
    #  1번째 인수: HttpRequest인스턴스
    #  2번째 인수: 문자열 (TEMPLATE['DIRS']를 기준으로 탐색할 템플릿 파일의 경로)
    #  3번째 인수: 템플릿을 렌더링할때 사용할 객체 모음
    # return render(request, 'blog/post_list.html', context)
    return render(
        request=request,
        template_name='blog/post_list.html',
        context=context,
    )


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post,
    }
    # post_detail view function이 올바르게 동작하는 html을 작성해서 결과 보기
    # 1. blog/post_detail.html
    return render(request, 'blog/post_detail.html', context)


def post_create(request):
    # title
    # text
    if request.method == 'POST':

        print(request.POST.get('title'))
        print(request.POST.get('text'))
        print(request.user)

        post = Post.objects.create(
            author=request.user,
            title=request.POST['title'],
            text=request.POST['text'],
        )
        # return HttpResponse('id: {}, title: {}, text: {}'.format(
        #     post.id,
        #     post.title,
        #     post.text,
        #     post.author,
        # ))
        # HTTP Redirection을 보낼 URL
        # http://localhost:8000/
        # / 로 시작하면 절대경로, 절대경로의 시작은 도메인(http:/localhost:8000/)
        return redirect('post-list')

    else:
        return render(request, 'blog/post_create.html')