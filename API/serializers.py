from rest_framework import serializers
from API.models import UserApi,UserCompanyApiModel
class UserApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApi
        fields = '__all__'


class UserCompanyApiSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    jobprofile = serializers.SerializerMethodField()
    class Meta:
        model = UserCompanyApiModel
        fields = ['id','name','company_name','jobprofile','address']

    def get_name(self,obj):
        return obj.name.name
    
    def get_jobprofile(self,obj):
        return obj.jobprofile.job