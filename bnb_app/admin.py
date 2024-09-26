from django.contrib import admin
from .models import Listing, Booking_status, Booking, Review, Rating
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Listing)
class book_data(ImportExportModelAdmin):
	pass


admin.site.register(Booking_status)
admin.site.register(Review)
admin.site.register(Booking)
admin.site.register(Rating)