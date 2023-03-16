#rest
from rest_framework import serializers

#my imports
from .models import User
from apps.transfer.serializers import HistoryTransferSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id',  'username', 'email', 
                  'phone_number', 'age','created_at'
                  )

class UserDetailSerializer(serializers.ModelSerializer):
    from_user = HistoryTransferSerializer(read_only=True, many=True)
    class Meta:
        model = User 
        fields = ('id',  'username', 'email', 
                  'phone_number', 'age', 'balance', 
                  'wallet_address','created_at','from_user'
                  )

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255, write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, write_only=True
    )
    class Meta:
        model = User 
        fields = ('id',  'username', 'email', 
                  'phone_number', 'age','created_at','password', 'password2'
                  )
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password' : 'Пароли отличаются'})
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError({"phone_number": "Напишите номер с +996"})
        return attrs

    def create(self, values):
        user = User.objects.create(
            username=values['username'], phone_number=values['phone_number'],
            age=values['age'], email=values['email'], 
            )
        user.set_password(values['password'])
        user.save()
        return user

