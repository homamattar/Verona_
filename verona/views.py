from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Project, Message
# Create your views here.

class HomeView(CreateView):
    template_name='index.html'
    # model = Project
    model = Message
    fields = ['name','email','phone','msg']

    def get_queryset(self):
        # project = Project.objects.all().order_by('-id')[:6]
        project = Project.objects.filter(featured=True).order_by('-id')[:7]
        return project
    
    def get_context_data(self, **kwargs):
        kwargs['object_list'] = self.get_queryset()
        return super(HomeView, self).get_context_data(**kwargs)

class ProjectsView(ListView):
    template_name='projectsPage.html'
    model = Project

    def get_queryset(self):
        project = Project.objects.filter(hide=False).order_by('-id')
        return project

class TestView(TemplateView):
    template_name='test.html'

class FeedbackView(CreateView):
    template_name='sections/feedback.html'
    fields = ['name','email','phone','msg']
    model = Message