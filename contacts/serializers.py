from rest_framework import serializers
from .models import Contact, Individual




class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model= Contact
        fields= ['name', 'number', 'email', 'sitelinks', 'date_of_birth', 'vital_connection']

class IndividualSerializer(serializers.ModelSerializer):
    contact= ContactSerializer()
    class Meta:
        model= Individual
        fields= ['id', 'username', 'password', 'contact']
        extra_kwargs={'password': {'write_only': True},
                    'id':{'read_only': True}
                    }
    
    def create(self, validated_data):
        contact_data = validated_data.pop('contact')
        contact = Contact.objects.create(**contact_data)
        individual = Individual.objects.create(contact=contact, **validated_data)
        return individual

    def update(self, instance, validated_data):
        contact_data = validated_data.pop('contact')
        contact = instance.contact
        for key, value in contact_data.items():
            setattr(contact, key, value)
        contact.save()
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
