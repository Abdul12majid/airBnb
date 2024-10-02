from django.contrib import admin
from .models import Listing, Booking_status, Booking, Review, Rating
from import_export.admin import ImportExportModelAdmin

# Register your models here.
#@admin.register(Listing)
#class book_data(ImportExportModelAdmin):
#	pass

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'location']
    list_filter = ['is_available']


admin.site.register(Booking_status)
admin.site.register(Review)
admin.site.register(Booking)
admin.site.register(Rating)