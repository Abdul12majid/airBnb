from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from bnb_app.models import Listing

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=255)
    date_of_birth=models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    profile_bio=models.TextField(null=True, blank=True, max_length=500)

    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()
post_save.connect(create_profile, sender=User)


class Bookings(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    bookings_made = models.ManyToManyField(Listing, symmetrical=False, blank=True)
    book_count = models.IntegerField(default=0)

    def __str__(self):
        return self.owner.user.username
