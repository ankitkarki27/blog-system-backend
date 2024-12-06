from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import*



# Create a DefaultRouter instance
router = DefaultRouter()

router.register(r'posts',PostViewSet,basename='posts')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'comments',CommentViewSet,basename='comments')
router.register(r'likes',LikeViewSet,basename='likes')
router.register(r'profiles',ProfileViewSet,basename='profiles')

urlpatterns = []
urlpatterns += router.urls

