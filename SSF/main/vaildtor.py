from django.core.validators import RegexValidator, EmailValidator
from .models import Landmark


class LandmarkValidator:

    def __init__(self, *args, **kwargs):    

        self.name = kwargs.get("name")
        self.place = kwargs.get("place")
        self.city = kwargs.get("city")
        self.about = kwargs.get("about")
        self.photo_url = kwargs.get("photo_url")
        self.errors = []
    
    def is_vaild(self):
 
        if Landmark.objects.filter(name=name).exists():
            self.errors.append("الاسم موجود مسبقا")

        return self.errors == 0


    def save(self):
        

        if Landmark.objects.filter(name=name).exists():
            self.errors.append("الاسم موجود مسبقا")

        return 