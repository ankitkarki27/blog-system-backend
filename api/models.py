from django.db import models
from django.contrib.auth.models import User
# Create your models for Blogging system here.

#category
class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='posts')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    image=models.ImageField(upload_to='upload/',blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

#commentmodel
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
    
    

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')  # Ensures one like per user per post

    def __str__(self):
        return f"{self.user} liked {self.post.title}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    
