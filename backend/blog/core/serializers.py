from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    #author = serializers.SlugRelatedField(
    #        slug_field='username',
    #        read_only=True
    #        )
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_author_name(self, obj):
        return obj.author.username



