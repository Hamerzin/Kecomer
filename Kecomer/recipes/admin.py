from recipes.models import RecipesModel, Ingredients, Favorites, QuantityModel, InstructionModel
from django.contrib import admin



@admin.register(RecipesModel)
class RecipesAdmin(admin.ModelAdmin):
    list_display= ['id','title','category','timeday']


admin.site.register(Ingredients)
admin.site.register(QuantityModel)
admin.site.register(InstructionModel)

@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display= ['id','platillo','ingredientes']
