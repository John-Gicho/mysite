from django.urls import path
from .views import home, services, projects, about, contact, signup, addUser #newsdate

urlpatterns = [
    path('home/', home, name="home"),
    path('services/', services, name="services"),
    path('projects/', projects, name="projects"),
    path('about/', about, name="about"),
    #path('newsdate<int:year>/', newsdate, name="newsdate"),
    path('contact/', contact, name="contact"),
    path('signup/', signup, name="signup" ),
    path('addUser/', addUser, name='addUser')

]