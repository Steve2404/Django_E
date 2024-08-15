# from django.http import HttpResponse
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from website.forms import SignupForm, BlogPostForm


class HomeView(TemplateView):
    template_name = r'website\base.html'
    title = 'Page d accueil'

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = self.title
        return content


def home(request):
    return render(request, 'website/base.html')


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Merci de vous etes inscrit sur le Site")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


def webseite_post(request):  # sourcery skip: merge-dict-assign, move-assign
    # si les donnee sont envoye au formulaire
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.published = True
            blogpost.save()
        return HttpResponseRedirect(request.path)
    else:
        # sinon les formulaires ne sont pas envoye
        init_values = {}
        if request.user.is_authenticated:
            init_values['author'] = request.user
        init_values['date'] = datetime.now()
        form = BlogPostForm(initial=init_values)
    return render(request, 'blog/blog.html', {'form': form})
