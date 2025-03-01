
    
    
    
class CategoryList(generics.ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer
    
    
    
