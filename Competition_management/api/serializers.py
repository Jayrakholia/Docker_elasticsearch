from rest_framework import serializers
from api.models import User, Competition, Entry

#user serializer
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    birth_date = serializers.DateField() 
    gender = serializers.CharField(max_length=100)
    #for create/post method
    def create(self, validation_data):
        return User.objects.create(**validation_data)
    #for update user data
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance

#comeptition serializer
class CompetitionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    #for create/post the data
    def create(self, validation_data):
        return Competition.objects.create(**validation_data)
    #for update the data
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.status = validated_data.get('status',instance.status)
        instance.description = validated_data.get('description',instance.description)
        instance.user_id = validated_data.get('user_id',instance.user_id)
        instance.save()
        return instance

#entry serializer    
class EntrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    topic = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    competition_id = serializers.PrimaryKeyRelatedField(queryset=Competition.objects.all())

    #for create/post data
    def create(self, validation_data):
        return Entry.objects.create(**validation_data)
    #for update data
    def update(self,instance,validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.topic = validated_data.get('topic',instance.topic)
        instance.state = validated_data.get('state',instance.state)
        instance.country = validated_data.get('country',instance.country)
        instance.competition_id = validated_data.get('competition_id',instance.competition_id)
        instance.save()
        return instance


