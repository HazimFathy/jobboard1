from .models import Blog , Category
import django_filters


class blogfilter(django_filters.filterset):
    class Meta:
        model=Blog
        fields='__all__'
        exclude=['owner',]
        
class BlogFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label='Category')

    class Meta:
        model = Blog
        fields = ['category']