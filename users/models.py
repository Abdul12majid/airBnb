from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from bnb_app.models import Listing, Booking_status


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=255)
    date_of_birth=models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    profile_bio=models.TextField(null=True, blank=True, max_length=500)
    bookings_made = models.ManyToManyField(Listing, symmetrical=False, blank=True)
    book_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()
post_save.connect(create_profile, sender=User)


class UserBooking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.ForeignKey(Booking_status, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.guest.username} booked {self.listing.title}')
