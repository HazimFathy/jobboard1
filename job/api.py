from .models import Job ,category
from .serializers import jobserializer ,CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def job_list_api(request):
    all_jobs=Job.objects.all()
    data=jobserializer(all_jobs,many=True).data
    return Response({'data':data})
    
@api_view(['GET'])   
def job_detail_api(request,id):
    job_detail=Job.objects.get(id=id)
    data=jobserializer(job_detail).data
    return Response({'data':data})
    
class joblist(generics.ListCreateAPIView):
    queryset=Job.objects.all()
    serializer_class=jobserializer
    
    
class jobdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Job.objects.all()
    serializer_class=jobserializer
    lookup_field='slug'
    
    
    
class CategoryList(generics.ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer
    
    
    