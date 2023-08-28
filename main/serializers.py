from rest_framework import serializers
from .models import Contact, Jokes

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class JokesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jokes
        fields = "__all__"