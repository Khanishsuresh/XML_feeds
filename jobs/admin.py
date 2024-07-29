from django.contrib import admin
from .models import Job
from .models import Employer

admin.site.register(Job)
admin.site.register(Employer)