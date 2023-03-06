from django.shortcuts import render, redirect
from .models import *
from django.views.generic import DetailView


def home(request):
    sliderdata = Event.objects.all()
    leaders = Leadership.objects.all()
    testimonydata = Testimony.objects.all()
    context = {'sliderdata': sliderdata,
               'leaders': leaders,
               'testimony': testimonydata}
    return render(request, 'casor/index.html', context)

def slider(request):
    sliderdata = Event.objects.all()
    context = {'sliderdata': sliderdata}
    return render(request, 'casor/slider.html', context)



def leadersView(request):
    leaders = Leadership.objects.all()
    context = {'leaders': leaders}
    return render(request, 'casor/leader.html', context)




def aboutUs(request):
    return render(request, 'casor/about.html')


def testimony(request):
    testimonies = Testimony.objects.all()
    context = {'testimonies': testimonies}
    return render(request, 'casor/testimony.html', context)

def event_list(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'casor/events.html', context)


#class EventDetailView(DetailView):
    #eventDetail = Event.objects.get(id=id)
    #context = {'eventDetail':eventDetail}
    #return render(request, 'casor/slider_detail.html', context)

class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'casor/slider_detail.html'

def praybox(request):
    if request.method =='POST':
        name =request.POST.get('name', '')
        prayer_topic = request.POST.get('prayer_topic','')
        phone_numbers=request.POST.get('phone_numbers', '')
        description=request.POST.get('description', '')
        prayerbox = RequestPayer(name=name, prayer_topic=prayer_topic, phone_numbers=phone_numbers, description=description,)
        prayerbox.save()
        return redirect('casor:prayerrequested')
    else:
        prayerbox = RequestPayer()
        return render(request, 'casor/prayer.html')



def success_prayer(request):
    return render(request, 'casor/requested.html')


#    def prayer_point(request):
 #       prayerpoints= RequestPayer.objects.filter(status="Processing").values_list("prayer_topic", flat=True)
        
  #      return render(request, 'casor/requested_prayer.html', {'prayer_points':prayerpoints})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
        contact_us = Contact(name=name, email=email, subject=subject, message=message)
        
        contact_us.save()
        return redirect('casor:thanks')
    else:
        contact_us =Contact()
    return render(request, 'casor/contact.html' )

def thanks(request):
    return render(request, 'casor/thanks.html')