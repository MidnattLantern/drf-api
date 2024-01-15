from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikesSerializer


class LikeList(generics.ListCreateAPIView):
    """
    Docstring
    """
    serializer_class = LikesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Docstring
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikesSerializer
    queryset = Like.objects.all()
