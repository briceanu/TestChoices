from rest_framework import serializers
from .models import Blog, LanguageChoices


class BlogSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Blog
        fields = '__all__'

    def validate_age(self,value):
        if value > 65:
            raise serializers.ValidationError(detail='Age can not be more than 65')
        return value

    def validate_language(self, value):
        # Custom validation to check if language is in allowed choices
        if value not in LanguageChoices.values:
            allowed_languages = ", ".join([label for _, label in LanguageChoices.choices])
            raise serializers.ValidationError(
                f"The selected language is not valid. The allowed languages are: {allowed_languages}."
            )
        return value