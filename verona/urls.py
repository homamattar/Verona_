from django.urls import path,include

from .views import HomeView,FeedbackView,ProjectsView, TestView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('test/', TestView.as_view(), name='test'),
    path('sendMessage/' , FeedbackView.as_view(), name='feedback'),
]
