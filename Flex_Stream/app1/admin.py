from django.contrib import admin
from app1.models import UserProfile, VideoDetail, StreamingSession
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(VideoDetail)
admin.site.register(StreamingSession)