from django.contrib import admin

# Register your models here.
from mysite.models import Article


admin.site.register([Article])