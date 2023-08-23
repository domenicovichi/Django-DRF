from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article, Journalist




class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    #author = JournalistSerializer()
    class Meta:
        model = Article
        #fields = "__all__"
        #fields = ("title", "description", "body")
        fields = ("title","body")
        #exclude = ("id",)

    def get_time_since_publication(self,object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date,now)
        return time_delta

    
    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Titolo e Descrizione devono essere diversi")
        return data
    
    def validate_title(self,value):
        if len(value) < 60:
            raise serializers.ValidationError("Scrivi un titolo che abbia almeno 60 caratteri")
        return value

class JournalistSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True) #articles = related_name
    #articles = serializers.HyperlinkedRelatedField(many=True,
    #                                read_only=True,
    #                               view_name="article-detail")
    class Meta:
        model = Journalist
        fields = "__all__"


# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self,validated_data):
#         """
#         crea e restituisce una nuova istanza di Article
#         sulla base dei dati validati
#         """
#         print(validated_data)
#         return Article.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         """
#         aggiorna e restituisce un'istanza di Article
#         aggiornata in base ai dati passati
#         """
#         instance.author = validated_data.get("author",instance.author)
#         instance.title = validated_data.get("title",instance.title)
#         instance.description = validated_data.get("description",instance.description)
#         instance.body = validated_data.get("body",instance.body)        
#         instance.location = validated_data.get("location",instance.location)
#         instance.publication_date = validated_data.get("publication_date",instance.publication_date)
#         instance.active = validated_data.get("active",instance.active)
#         instance.save()
#         return instance
