from rest_framework import serializers
from myapp.models import web1 ,LANGUAGE_CHOICES

'''class Web1Serializers(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    news_head=serializers.CharField(required=False, allow_blank=True, max_length=100)
    news_web=serializers.CharField(required=False, allow_blank=True, max_length=100)
    date=serializers.DateField()

    def create(self,validated_data):
        return web1. objects , create(validated_data)

    def update(self,instance,validated_data):
            instance.news_head=validated_data.get( 'news_head' ,instance.news_head)
            instance.news_web=validated_data.get( 'news_web' ,instance.news_web)
            instance.date=validated_data.get( 'date' ,instance.date)
            instance.language=validated_data.get('language',instance.language)
            instance.save()
            return instance'''


class Web1Serializers(serializers.ModelSerializer):
    class Meta:

        fields = ['id', 'news_head', 'news_web', 'date', 'language']
