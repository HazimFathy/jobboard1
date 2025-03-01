import django_filters
from .models import Job, category



class jobFilter(django_filters.FilterSet):
    description= django_filters.CharFilter(lookup_expr='icontains')
    title= django_filters.CharFilter(lookup_expr='icontains')
    country = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude=['Published_on','image','slug','owner','id']
        
class JobFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(queryset=category.objects.all(), label='Category')

    class Meta:
        model = Job
        fields = ['category']