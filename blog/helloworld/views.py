from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwner
from .filters import PostFilter


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = PostFilter
    search_fields = ['title', 'content']
    ordering_fields = ['id']

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.filter(owner=user)
        return post

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.filter(owner=user)
        return post
