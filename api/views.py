# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action


from .models import Category,Post,Profile,Comment,Like
from .serializers import (
    CategorySerializer,
    PostSerializer,
    LikeSerializer,
    CommentSerializer,
    ProfileSerializer,
)
# Create your views here.
#after making serializer,it is imported in views

class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    

class PostViewSet(ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    @action(detail=True,methods=['get'],
            permission_classes=[IsAuthenticatedOrReadOnly])
    
    def comments(self ,request ,pk=None):
        """
        Fetches all comments associated with a specific post.
        Only accessible for authenticated users or read-only for unauthenticated users.
        """
        Post=self.get_object() # Get the post object by primary key (pk)
        if not post:
            raise NotFound('post not found')
        
        comments=post.comments.all()
        Serializer == CommentSerializer(comments,Many=True) # Serialize the comments
        return Response(serializer.data) # Return the serialized comments as response

    @action(detail=True,methods=['get'],
            permission_classes=[IsAuthenticatedOrReadOnly])
    
    def likes(self ,request ,pk=None):
        """
        Fetches all likes associated with a specific post.
        Only accessible for authenticated users or read-only for unauthenticated users.
        """
        post=self.get_object() # Get the post object by primary key (pk)
        if not post:
            raise NotFound('post not found')
        
        likes=post.likes.all()
        Serializer == LikesSerializer(likes,Many=True) # Serialize the comments
        return Response(serializer.data) # Return the serialized comments as response

class CommentViewSet(ModelViewSet):
    queryset=Comment.objects.all()   # Fetches all comments
    serializer_class=CommentSerializer    # Serializes comment data
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read for all, modify only for authenticated users
    
    def perform_create(self, serializer):
        # Automatically associates the logged-in user as the author of the comment
        serializer.save(author=self.request.user)
        
        
class LikeViewSet(ModelViewSet):
    queryset=Like.objects.all()
    serializer_class=LikeSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        # Automatically associates the logged-in user with the like
        serializer.save(user=self.request.user)
        
class ProfileViewSet(ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    
    def perform_update(self, serializer):
        # Ensures users can only update their own profile
        if self.request.user == self.get_object().user:
            # If the user is updating their own profile, save the update
            serializer.save()
        else:
            # If not, raise a PermissionDenied exception
            raise PermissionDenied('You cannot update this profile')
    
        
        