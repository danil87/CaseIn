from django.contrib import admin
from .models import Articles
from .models import Members

admin.site.register(Articles)
admin.site.register(Members)