from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserPost)
admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(BlogCommentReply)
