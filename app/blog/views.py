from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
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
            title=request.POST['title']
            text=request.POST['text']
        )
        return HttpResponse('id: {}, title: {}, text: {}'.format(
            post.id,
            post.title,
            post.text,
            post.author,
        ))

        # new_post = Post.objects.create(title=request.POST.get('title'),
        #                                text=request.POST.get('text'),
        #                                author=request.user
        #                                )
        # new_post.save()

        # return HttpResponse(request.GET.get('title'))

        # request의 method값이 'POST'일 경우 (POST method로 요청이 왔을 경우)
        # request.POST 에 있는 title, text값과
        # request.user 에 있는 User 인스턴스(로그인한 유저)속성을 사용해서
        # 새 Post인스턴스를 생성
        # HttpResponse를 사용해 새로 생성된 인스턴스의 id, title, text정보를 출력(string)
        # return render(request, 'blog/post_detail.html')
    else:
        return render(request, 'blog/post_create.html')