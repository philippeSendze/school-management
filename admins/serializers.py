from rest_framework import serializers

from admins.models import Accountant, Administrator, Director, Secretary

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
        
        
class SecretarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Secretary
        fields = '__all__'
        

class AdministratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Administrator
        fields = '__all__'
        

class AccountantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accountant
        fields = '__all__'