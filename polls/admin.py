from django.contrib import admin

from .models import Question

admin.site.register(Question)  # Tells admin that Question objects have an admin interface
