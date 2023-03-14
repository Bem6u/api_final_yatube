from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['post']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )
    group = serializers.SlugRelatedField(
        slug_field="id", queryset=Group.objects.all(), required=False
    )

    class Meta:
        fields = '__all__'
        model = Post


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        read_only=True,
        slug_field="username",
        default=serializers.CurrentUserDefault(),
    )
    following = SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ("user", "following")
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("user", "following"),
                message="Уже подписаны",
            )
        ]

    def validate(self, data):
        user = self.context["request"].user
        follow_obj = data["following"]
        if user == follow_obj:
            raise serializers.ValidationError(
                "Невозможно подписаться на самого себя"
            )
        return data
