from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Follow
from .serializers import FollowSerializer


class FollowList(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)


class FollowCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        following_id = request.data.get('following')
        if following_id == request.user.id:
            return Response({'error': 'Нельзя подписаться на самого себя'})
        serializer = FollowSerializer(data={
            'user': request.user.id,
            'following': following_id,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
