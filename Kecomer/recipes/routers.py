from rest_framework.routers import DefaultRouter

from recipes.genericviews import RecipesViewset

router = DefaultRouter()
router.register(r'recipes', RecipesViewset, basename='recipes')