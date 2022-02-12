from django.db import models

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=20)
    ingredient1 = models.CharField(max_length=20)
    ingredient2 = models.CharField(max_length=20)
    ingredient3 = models.CharField(max_length=20)
    ingredient4 = models.CharField(max_length=20)
    ingredient5 = models.CharField(max_length=20)
    course = models.IntegerField(default=0)
    type = models.IntegerField(default=0)
    regist = models.DateField()
    update = models.DateField()
    
    def __str__(self):
        return 'id: ' + str(self.id) + ', ' + \
               'name: ' + str(self.name) + ', ' + \
               'ingredient1: ' + str(self.ingredient1) + ', ' + \
               'ingredient2: ' + str(self.ingredient2) + ', ' + \
               'ingredient3: ' + str(self.ingredient3) + ', ' + \
               'ingredient4: ' + str(self.ingredient4) + ', ' + \
               'ingredient5: ' + str(self.ingredient5) + ', ' + \
               'course: ' + str(self.course) + ', ' + \
               'type: ' + str(self.type)