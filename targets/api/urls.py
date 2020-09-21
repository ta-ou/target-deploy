
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from targets.api import views as qv

router = DefaultRouter()
router.register(r"targets", qv.TargetViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("targets/<slug:slug>/comments/", qv.CommentListAPIView.as_view(), name="comment-list"),
    path("targets/<slug:slug>/comment/", qv.CommentCreateAPIView.as_view(), name="comment-create"),
    path("comments/<int:pk>/", qv.CommentRUDAPIView.as_view(), name="comment-detail"),
    path("targets/<slug:slug>/like/", qv.TargetLikeAPIView.as_view(), name="target-like"),
]

