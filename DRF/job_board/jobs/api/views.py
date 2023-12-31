from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from jobs.models import JobOffer
from jobs.api.serializers import JobOfferSerializer

class JobListCreateAPIView(APIView):
    def get(self,request):
        jobs = JobOffer.objects.filter(available=True)
        serializer = JobOfferSerializer(jobs,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = JobOfferSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class JobDetailAPIView(APIView):
    def get_object(self,pk):
        job = get_object_or_404(JobOffer, pk=pk)
        return job

    def get(self,request,pk):
        job = self.get_object(pk)
        serializer = JobOfferSerializer(job)
        return Response(serializer.data)
    
    def put(self,request,pk):
        job = self.get_object(pk)
        serializer = JobOfferSerializer(job,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
