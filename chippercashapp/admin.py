from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Post)
admin.site.register(Email_post)
admin.site.register(Pin_post)
admin.site.register(Otp_post)