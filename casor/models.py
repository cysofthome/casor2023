from django.db import models
from django.urls import reverse


class Event(models.Model):
    event_title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    event_host = models.CharField(max_length=250, null=True, blank=True)
    event_date = models.DateTimeField()
    event_location = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='Events_images', null=True, blank=True)
    
    class Meta:
        ordering = ('-event_date',)

    def __str__(self):
        return f" {self.event_host}, {self.event_title}"
    
    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.slug)])
    
    


class Leadership(models.Model):
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='leaders')
    year_start = models.DateField()
    year_end = models.DateField()
    whatsapp_number = models.CharField(max_length=11)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.CharField(max_length=128)
    state_of_origin = models.CharField(max_length=64)
    local_govt = models.CharField(max_length=64)
    residential_address = models.CharField(max_length=250)

    def __str__(self):
        return self.position


PRAYER_STATUS = (
    ('answered', 'Answered '),
    ('pending', 'Pending'),
    ('processing', 'Processing')

)


class RequestPayer(models.Model):
    name = models.CharField(max_length=250)
    prayer_topic = models.CharField(max_length=250)
    phone_numbers = models.CharField(max_length=12, null=True, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=16, choices=PRAYER_STATUS, default='Pending')

    def __str__(self):
        return self.name


class Testimony(models.Model):
    name = models.CharField(max_length=250)
    miracle = models.TextField()
    photo = models.ImageField(upload_to='testimony')

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.name
