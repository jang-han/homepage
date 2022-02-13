from django.db import models

# Create your models here.
class Ingredient(models.Model):
    ingredient = models.CharField(max_length=20)
    regist = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'id: ' + str(self.id) + ', ' + \
               'ingredient: ' + str(self.ingredient) + ', ' + \
               'regist: ' + str(self.regist) + ', ' + \
               'update: ' + str(self.update)


class Course(models.Model):
    course = models.CharField(max_length=20)
    regist = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'id: ' + str(self.id) + ', ' + \
               'course: ' + str(self.course) + ', ' + \
               'regist: ' + str(self.regist) + ', ' + \
               'update: ' + str(self.update)

               
class Type(models.Model):
    type = models.CharField(max_length=20)
    regist = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'id: ' + str(self.id) + ', ' + \
               'type: ' + str(self.type) + ', ' + \
               'regist: ' + str(self.regist) + ', ' + \
               'update: ' + str(self.update)

        
class Dish(models.Model):
    name = models.CharField(max_length=20)
    ingredient1 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient1")
    ingredient2 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient2")
    ingredient3 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient3")
    ingredient4 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient4")
    ingredient5 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient5")
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    regist = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'id: ' + str(self.id) + ', ' + \
               'name: ' + str(self.name) + ', ' + \
               'ingredient1: ' + str(self.ingredient1) + ', ' + \
               'ingredient2: ' + str(self.ingredient2) + ', ' + \
               'ingredient3: ' + str(self.ingredient3) + ', ' + \
               'ingredient4: ' + str(self.ingredient4) + ', ' + \
               'ingredient5: ' + str(self.ingredient5) + ', ' + \
               'course: ' + str(self.course) + ', ' + \
               'type: ' + str(self.type) + ', ' + \
               'regist: ' + str(self.regist) + ', ' + \
               'update: ' + str(self.update)
    
    class Meta:
        ordering = ('update',)