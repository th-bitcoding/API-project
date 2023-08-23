from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from API.serializers import UserApiSerializer,UserCompanyApiSerializer
from rest_framework.response import Response
from API.models import UserApi,UserCompanyApiModel, JobProfile
from rest_framework import status
# Create your views here.

# ======================================================================
class UserDetailApi(APIView):
    permission_classes = []
    def get_queryset(self):
        return UserApi.objects.all()

    def get(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = UserApiSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = UserApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    

# ===========================================================================

class UserCompanyApi(APIView):
    permission_classes = []

    def get_object(self, pk):
        try:
            return UserCompanyApiModel.objects.get(pk=pk)
        except UserCompanyApiModel.DoesNotExist:
            raise Http404


    def get_queryset(self):
        return UserCompanyApiModel.objects.all()
    
    def get(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = UserCompanyApiSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserCompanyApiSerializer(data=request.data)

        if serializer.is_valid():
            name = request.data.get('name')
            jobdata = request.data.get('jobprofile')

            try:
                get_name = UserApi.objects.get(name=name)
            except UserApi.DoesNotExist:
                return Response({'message': 'UserApi entry with provided name not found'}, status=status.HTTP_404_NOT_FOUND)
            try:
                get_profile = JobProfile.objects.get(job=jobdata)
            except JobProfile.DoesNotExist:
                return Response({'message': 'Profile entry not found'}, status=status.HTTP_404_NOT_FOUND)

            if get_name.name != name or get_profile.job != jobdata:
                print('Names do not match')
            else:
                serializer.save(name=get_name, jobprofile=get_profile)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk):
        check_id =self.get_object(pk)
        serializer = UserCompanyApiSerializer(check_id,data=request.data)

        if serializer.is_valid():
            get_name = UserApi.objects.get(name=request.data.get('name'))
            get_profile = JobProfile.objects.get(job = request.data.get('jobprofile'))
            serializer.save(name=get_name,jobprofile = get_profile)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        data =self.get_object(pk)
        data.delete()
        return Response({'message': 'Object deleted successfully'},status=status.HTTP_204_NO_CONTENT)

