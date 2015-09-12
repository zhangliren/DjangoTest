from django.contrib import admin

from mymsgs.models import User, Message

admin.site.register(User)
admin.site.register(Message)
