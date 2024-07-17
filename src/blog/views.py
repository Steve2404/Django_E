from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from blog.models import BlogPost


# Create your views here.
# def blog_post(request):
#     numero_article = 2
#     try:
#         blog = BlogPost.objects.get(pk=numero_article)
#     except BlogPost.DoesNotExist as e:
#         raise Http404(f"L article numero {numero_article} est introuvable ") from e
#     return HttpResponse(blog.content)


@login_required
def blog_post_error(request):
    blog = get_object_or_404(BlogPost, slug='les-bases-de-django')
    return HttpResponse("hello !!!")


@user_passes_test(lambda user: user.username == 'Leonel')
def passes_test(request):
    blog = get_object_or_404(BlogPost, pk=5)
    return HttpResponse(blog.content)


@user_passes_test(lambda user: "Moderateur" in [group.name for group in user.groups.all()])
def passes_test_group(request):
    blog = get_object_or_404(BlogPost, pk=8)
    return HttpResponse(blog.content)


def blog_post(request):
    return redirect('home')


def blog_posts(request, pk):
    blog = BlogPost.objects.get(pk=pk)
    resp = render_to_string('blog/post.html', {'blog': blog})
    response = HttpResponse(resp)
    return response


def blog_posts2(request):
    blog = BlogPost.objects.filter(pk__in=[5, 6, 7, 8, 9])
    return render(request, 'blog/post2.html', {'blog': blog})


def blog_posts1(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    return render(request, 'blog/post.html', {'blog': blog})


def blog_posts3(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    return render(request, 'blog/post3.html', {'blog': blog})
