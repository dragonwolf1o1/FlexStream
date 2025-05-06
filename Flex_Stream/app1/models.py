from django.db import models

# Create your models here.

class UserProfile(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    phone=models.CharField(max_length=15,unique=True)
    ip_address=models.GenericIPAddressField(null=True, blank=True)
    user_agent=models.CharField(max_length=500, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class VideoDetail(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    tags=models.CharField(max_length=100,help_text="Comma-separated tags")
    video_file=models.FileField(upload_to='videos/')
    thumbnail=models.ImageField(upload_to='thumbnails/')
    uploaded_at=models.DateTimeField(auto_now_add=True)
    userprofile=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='videos')
    
    def __str__(self):
        return self.title
    
    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(',')]
    
class StreamingSession(models.Model):
    id=models.AutoField(primary_key=True)
    userprofile=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='streamingsessions')
    video_detail=models.ForeignKey(VideoDetail,on_delete=models.CASCADE,related_name='streamingsessions')
    start_time=models.DateTimeField(auto_now_add=True)
    end_time=models.DateTimeField(null=True,blank=True)
    watched_minutes = models.PositiveIntegerField(default=0)
    status=models.CharField(max_length=20,choices=[('active','Active'),('inactive','Inactive')],default='active')
    video_detail = models.ForeignKey(VideoDetail, on_delete=models.CASCADE, related_name='streamingsessions')

    
    def __str__(self):
        return f"{self.userprofile.username} - {self.video_detail.title}"
