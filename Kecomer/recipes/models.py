from django.db import models


#Tabla ingredientes relacionada con RecipesModel para traer nombre de receta
class Ingredients(models.Model):
    dishe_1 = models.CharField(max_length=255)

    def __str__(self):
        return self.dishe_1

    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'ingredientes'
        ordering = ['id']


class InstructionModel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'InstructionModel'
        verbose_name_plural = 'InstructionModels'
        ordering = ['id']


class QuantityModel(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'QuantityModel'
        verbose_name_plural = 'QuantityModels'
        ordering = ['id']


# Create your models here.
class RecipesModel(models.Model):
    time_choice = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner')
    ]
    category_choice = [
        ('VEGANA', 'Vegana'),
        ('CARNE', 'Carne'),
        ('POSTRE', 'Postre'),
    ]

    difficulty_choice = [
        ('Fácil', 'Fácil'),
        ('Normal', 'Normal'),
        ('Dificíl', 'Dificíl'),
    ]

    title=models.CharField(max_length=255, unique=True)
    image=models.ImageField(upload_to="recipes/img", blank=True, null=True)
    link_video=models.CharField(max_length=255, blank=True, null=True)
    category=models.CharField(max_length=12, choices=category_choice)
    timeday= models.CharField(max_length=12, choices=time_choice)
    difficulty = models.CharField(max_length=10, choices=difficulty_choice)
    recipes_time=models.IntegerField()
    ingredients=models.ManyToManyField(Ingredients)
    quantity = models.ManyToManyField(QuantityModel)
    instruction = models.ManyToManyField(InstructionModel)
    like=models.IntegerField(default=0, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ['id']



class Favorites(models.Model):
    platillo=models.ForeignKey(RecipesModel,on_delete=models.CASCADE)
    ingredientes=models.ForeignKey(Ingredients, on_delete=models.CASCADE)

    def __str__(self):
        return f"favorito-> {self.platillo}"
    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
        ordering = ['id']
        


