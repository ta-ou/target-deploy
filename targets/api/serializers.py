from rest_framework import serializers
from targets.models import Comment, Target


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    target_slug = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ["target"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%Y年%m月%d日")

    def get_target_slug(self, instance):
        return instance.target.slug


class TargetSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    comment_count = serializers.SerializerMethodField()
    user_has_commented = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()
    

    class Meta:
        model = Target
        exclude = ["voters"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%Y年%m月%d日")

    def get_comment_count(self, instance):
        return instance.comments.count()

    def get_user_has_commented(self, instance):
        request = self.context.get("request")
        return instance.comments.filter(author=request.user).exists()

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()

