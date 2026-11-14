from rest_framework import serializers
from .models import FirewallRequest

#class DogSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Dog
#        fields = '__all__'
        
class FirewallRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirewallRequest
        fields = ['id', 'title', 'requester', 'source_ip', 'destination_ip',
                  'port', 'protocol', 'justification', 'rule_purpose', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']     #This line should prevent users from setting their own status or dates. This is one of the mitigations I mentioned.