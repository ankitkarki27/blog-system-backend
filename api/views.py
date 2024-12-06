from django.shortcuts import render
from .models import Category,Post,Profile,Comment,Like
from serializers import (
    CategorySerializer,
    PostSerializer,
    LikeSerializer,
    CommentSerializer,
    ProfileSerializer,
)
# Create your views here.
#after making serializer,it is imported in views