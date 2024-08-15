from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import BlogPost
from website.forms import BlogPostForm


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


class BlogIndexView(ListView):
    model = BlogPost
    template_name = 'blog/index.html'
    context_object_name = 'posts'


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/post.html"
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        try:
            obj = queryset.filter(slug=slug).first()
        except queryset.model.DoesNotExist as e:
            raise Http404('No post found with this title') from e
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/blog.html'
    form_class = BlogPostForm
    title = "Creer un article"
    valeur = "Creer"

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = self.title
        content['valeur'] = self.valeur
        return content

    def get_success_url(self):
        return reverse('blog-listes')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        form.instance.published = True
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog.html'
    title = "Editer cet article"
    valeur = "Update"

    def form_valid(self, form):
        # Met à jour le slug avant de sauvegarder l'objet
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = self.title
        content['valeur'] = self.valeur
        return content

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        try:
            obj = queryset.filter(slug=slug).first()
        except queryset.model.DoesNotExist as e:
            raise Http404('No post found with this title') from e
        return obj


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog-listes')


def blog_posts2(request):
    blog = BlogPost.objects.filter(pk__in=[5, 6, 7, 8, 9])
    return render(request, 'blog/post2.html', {'blog': blog})


def blog_posts1(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    return render(request, 'blog/post.html', {'blog': blog})


def blog_posts3(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    return render(request, 'blog/post3.html', {'blog': blog})
