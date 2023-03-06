from django.urls import path
from . import views
from .views import EventDetailView

app_name = 'casor'


urlpatterns = [
    path('', views.home, name='home'),
    path('leaders', views.leadersView, name='leaders'),
    path('slider', views.slider, name='slider'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('testimony', views.testimony, name='testimony'),
    path('events', views.event_list, name='events'),
    
    path('prayer', views.praybox, name='prayerbox'),
    
    path('prayer-requested', views.success_prayer, name='prayerrequested'),
    
    #path('prayer-point', views.prayer_point, name='prayer_point'),
    

    path('<slug:slug>/', EventDetailView.as_view(), name='event_detail'),
    path('contact', views.contact, name='contact'),
    path('thanks', views.thanks, name='thanks'),
]
