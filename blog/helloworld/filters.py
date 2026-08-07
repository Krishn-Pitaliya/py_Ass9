from django_filters import rest_framework as filters

from .models import Post


class PostFilter(filters.FilterSet):
    created_at = filters.DateFilter(
        field_name='created_at',
        lookup_expr='date'
    )

    class Meta:
        model = Post
        fields = ['created_at']
