from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review

class Command(BaseCommand):
    "Populate the DB wih Sample Data"

    def db_populate(self, *args, **kwargs):      

        # Create sample listings
        listings = [
            Listing(title="Kempinski Hotel", description="Five star modern hotel", price_per_night=20000.00, location="Nairobi"),
            Listing(title="Lalanasi Resort", description="Your Offroad place to be", price_per_night=15000.00, location="Laikipia"),
            Listing(title="Spring Valley Resort", description="Want a serene, quality and modern hotel, Spring Valley is the one for you", price_per_night=25000.00, location="Spring Valley"),
        ]
        Listing.objects.bulk_create(listings)

        # Dummy data for Booking model
        Booking.objects.create(listing=listings[0], user_name="Rose Kim", check_in_date="2024-12-25", check_out_date="2024-12-29")
        Booking.objects.create(listing=listings[1], user_name="Alex Jones", check_in_date="2024-12-23", check_out_date="2024-12-25")

        # Dummy data for Reviews model
        Review.objects.create(listing=listings[0], user_name="Rose Kim", rating=5, comment="Cool Place to be!")
        Review.objects.create(listing=listings[1], user_name="Alex Jones", rating=4, comment="Quality services,but no internet.")

        self.stdout.write(self.style.SUCCESS("Database Populated Successfully!"))