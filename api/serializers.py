from rest_framework import serializers
from .models import Category, Post, Comment, Like, Profile
from django.contrib.auth.models import User

# after making serializer import it to views.py
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id','name','slug']
        
class PostSerializer(serializers.ModelSerializer):
    author=serializers.StringRelatedField()
    categories = CategorySerializer(many=True,read_only=True)
    categories_ids=serializers.PrimaryKeyRelatedField(many=True,
                                                      queryset=Category.objects.all(),write_only=True,source='categories')
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 
            'author', 'categories', 'category_ids','status', 'image', 
            'created_at', 'updated_at'
        ]
    

class CommentSerializer(serializers.ModelSerializer):
    Post=serializers.StringRelatedField()
    author=serializers.StringRelatedField()
    
    class Meta:
        model = Comment
        fields=[
            'id','post','author','content'
        ]

class LikeSerializer(serializers.ModelSerializer):
    Post=serializers.StringRelatedField()
    user=serializers.StringRelatedField()
    
    class Meta:
        model=Like
        fields=[
            'id','post','user'
        ]
        
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        # The Meta class is used to configure the serializer.
        # It tells the serializer which model to use and what fields to include.
        model = Profile  # Specifies the Profile model to serialize
        fields = [       
            'id',           
            'user',         
            'profile_picture'
        ]

        
        