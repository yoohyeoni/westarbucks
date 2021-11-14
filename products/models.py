from django.db import models



from django.db import models
class Menu(models.Model):
    name = models.CharField(max_length=45)
    class Meta:
          db_table = 'menus'
class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    class Meta:
          db_table = 'categories'
class Drink(models.Model):
    korean_name  = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45, blank=True)
    category     = models.ForeignKey('Category', on_delete=models.CASCADE)
    desciption   = models.TextField(blank=True)
    class Meta:
          db_table = 'drinks'
class AllergyDrink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink   = models.ForeignKey('Drink', on_delete=models.CASCADE)
    class Meta:
          db_table = 'allergy_drinks'

class Image(models.Model):
    image = models.CharField(max_length=2000)
    drink  = models.ForeignKey('Drink', on_delete=models.CASCADE)
    class Meta:
          db_table = 'images'
class Allergy(models.Model):
    name = models.CharField(max_length=45)
    class Meta:
          db_table = 'allergies'











































# Create your models here.
