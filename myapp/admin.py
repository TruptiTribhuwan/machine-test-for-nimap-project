from django.contrib import admin

from myapp.models import client
admin.site.register(client)


from myapp.models import User
admin.site.register(User)

# Register your models here.
