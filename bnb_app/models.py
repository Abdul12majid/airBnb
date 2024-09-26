from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    amenities = models.TextField()
    host = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
    	return self.title

    class Meta:
    	verbose_name_plural = "Properties"


class Booking_status(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "Booking_status"

	def __str__(self):
		return self.name


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.ForeignKey(Booking_status, on_delete=models.CASCADE)

class Rating(models.Model):
    star = models.CharField(max_length=255)

    def __str__(self):
        return self.star


class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return (f"{self.guest.username} review on {self.listing.title}")













