from django.contrib.auth.models import User, Group
from rest_framework import serializers
from products.models import Products, UserModel


class UserData(serializers.ModelSerializer):
    class Meta:
        model = User
        userDetail = User.objects.all()
        fields = ('username', 'password')


class UserSerializer(serializers.ModelSerializer):
    user = UserData()
    class Meta:
        model = UserModel
        fields = ('user', 'location', 'profile_picture')



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'picture', 'added', 'code', 'cost', 'category')

    def validate(self, data):
        import ipdp
        if(data['name'])
