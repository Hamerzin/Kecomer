from rest_framework import serializers
from .models import RecipesModel


class RecipesSerializer(serializers.ModelSerializer):
    ingredients = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()
    instruction = serializers.SerializerMethodField()

    def get_ingredients(self, instance):
        queryset = instance.ingredients.get_queryset()
        names = [ingredient.dishe_1 for ingredient in queryset]
        return names

    def get_quantity(self, instance):
        queryset = instance.quantity.get_queryset()
        names = [quantitys.name for quantitys in queryset]
        return names

    def get_instruction(self, instance):
        queryset = instance.instruction.get_queryset()
        names = [instructions.name for instructions in queryset]
        return names

    class Meta:
        model = RecipesModel
        fields = ["id","title", "link_video", "image", "category", "timeday", 'difficulty', 'duration', "like", "description", 'ingredients', 'quantity', 'instruction']