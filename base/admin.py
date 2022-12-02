from django.contrib import admin

# Register your models here.
from base.models import *

admin.site.register([User, practicearea, ourpurpose, expert, question, review])
