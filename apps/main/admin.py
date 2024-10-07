from django.contrib import admin

from apps.main.models import Product

admin.site.register(Product)



admin.site.site_header = "JVToken Admin"
admin.site.site_title = "JVToken Admin Portal"
admin.site.index_title = "Welcome to JVToken Portal"
