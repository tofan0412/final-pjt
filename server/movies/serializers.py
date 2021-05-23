from rest_framework import serializers
from .models import Movie, Review


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

# class RateSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Movie
#         fields = ('userRating')
        