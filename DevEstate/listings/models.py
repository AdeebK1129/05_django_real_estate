from django.db import models
import random
from django.db.models import Max


class Property(models.Model):
    zpid = models.IntegerField(primary_key=True)
    imgSrc = models.CharField(max_length=255, null=True)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    living_area = models.IntegerField(null=True)
    bedrooms = models.IntegerField(null=True)
    bathrooms = models.IntegerField(null=True)
    year_built = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    date_posted = models.DateTimeField(null=True)
    date_sold = models.DateTimeField(null=True, blank=True)
    home_type = models.CharField(max_length=255, null=True)
    property_tax_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    time_on_zillow = models.CharField(max_length=255, null=True)
    home_status = models.CharField(max_length=255, null=True)
    annual_homeowners_insurance = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    rent_zestimate = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    brokerage_name = models.CharField(max_length=255, null=True, blank=True)
    page_view_count = models.IntegerField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f"[{self.zpid}, {self.imgSrc}]"
    
    def save(self, *args, **kwargs):
        if self.zpid is None:
            # Generate a random zpid. Adjust range as needed for your use case.
            max_id = Property.objects.aggregate(max_zpid=Max('zpid'))['max_zpid']
            self.zpid = (max_id if max_id is not None else 0) + random.randint(1, 100)

            # Make sure the generated zpid does not already exist.
            while Property.objects.filter(zpid=self.zpid).exists():
                self.zpid += random.randint(1, 100)
        
        super().save(*args, **kwargs)

class PropertyFeatures(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    flooring = models.CharField(max_length=255, null=True, blank=True)
    foundation_details = models.CharField(max_length=255, null=True, blank=True)
    accessibility_features = models.CharField(max_length=255, null=True, blank=True)
    garage_spaces = models.IntegerField(null=True, blank=True)
    parking_spaces = models.IntegerField(null=True, blank=True)
    view_type = models.CharField(max_length=255, null=True, blank=True)
    water_view = models.BooleanField(null=True, blank=True)
    heating = models.CharField(max_length=255, null=True, blank=True)
    cooling = models.CharField(max_length=255, null=True, blank=True)
    construction_materials = models.CharField(max_length=255, null=True, blank=True)
    roof_type = models.CharField(max_length=255, null=True, blank=True)
    lot_size = models.CharField(max_length=255, null=True, blank=True)
    hoa_fee = models.CharField(max_length=255, null=True)

class Agent(models.Model):
    display_name = models.CharField(max_length=255, null=True)
    review_count = models.IntegerField(null=True)
    rating_average = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    image_url = models.CharField(max_length=255, null=True)
    badge_type = models.CharField(max_length=255, null=True)

class PropertyAgent(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

class School(models.Model):
    name = models.CharField(max_length=255, null=True)
    rating = models.IntegerField(null=True)
    students_per_teacher = models.IntegerField(null=True)
    size = models.IntegerField(null=True)
    level = models.CharField(max_length=255, null=True)
    grades = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    distance = models.DecimalField(max_digits=5, decimal_places=2, null=True)

class PropertySchool(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class PriceHistory(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)
    event = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    price_per_square_foot = models.DecimalField(max_digits=19, decimal_places=2, null=True)

class NearbyHomes(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    zpid = models.IntegerField(primary_key=True)
    imgSrc = models.CharField(max_length=255, null=True)
    street_address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    zipcode = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    living_area = models.IntegerField(null=True)  
    price = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    home_type = models.CharField(max_length=255, null=True)
    home_status = models.CharField(max_length=255, null=True)


