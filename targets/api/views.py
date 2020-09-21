from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from targets.api.permission import IsAuthorOrReadOnly
from targets.api.serializers import CommentSerializer, TargetSerializer
from targets.models import Comment, Target

class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = TargetSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        target = get_object_or_404(Target, slug=kwarg_slug)

        if target.comments.filter(author=request_user).exists():
            raise ValidationError("Already comment!")

        serializer.save(author=request_user, target=target)


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Comment.objects.filter(target__slug=kwarg_slug).order_by("-created_at")


class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class TargetLikeAPIView(APIView):
    serializer_class = TargetSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, slug):
        target = get_object_or_404(Target, slug=slug)
        user = request.user

        target.voters.remove(user)
        target.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(target, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug):
        target = get_object_or_404(Target, slug=slug)
        user = request.user

        target.voters.add(user)
        target.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(target, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
